from __future__ import absolute_import, division, print_function, unicode_literals

import os
import pathlib
import typing

import numpy as np
import tensorflow as tf

AUTOTUNE = tf.data.experimental.AUTOTUNE

"""
The imagewoof dataset is provided by FastAI

author    = "Jeremy Howard",
title     = "imagenette",
url       = "https://github.com/fastai/imagenette/"
"""


class ImageWoof:
    BATCH_SIZE: int = 32
    CLASS_NAMES: np.ndarray = None
    data_dir: pathlib.Path
    image_count: int = 0
    list_ds: tf.data.Dataset = None

    def __init__(self, dataset: str) -> None:
        if dataset != "train" and dataset != "val":
            raise ValueError("Dataset not found")

        file_path = tf.keras.utils.get_file(
            origin="https://s3.amazonaws.com/fast-ai-imageclas/imagewoof2-320.tgz",
            fname="imagewoof",
            untar=True,
        )
        self.data_dir = pathlib.Path(file_path + "2-320/" + dataset)
        print(self.data_dir)
        self.image_count = len(list(self.data_dir.glob("*/*.JPEG")))
        print(self.image_count)

        self.CLASS_NAMES = np.array(
            [
                item.name
                for item in self.data_dir.glob("*")
                if item.name != "LICENSE.txt"
            ]
        )
        print(self.CLASS_NAMES)

        self.list_ds = tf.data.Dataset.list_files(str(self.data_dir / "*/*"))

    def get_label(self, file_path: str) -> tf.Tensor:
        # convert the path to a list of path components
        parts = tf.strings.split(file_path, os.path.sep)
        # The second to last is the class-directory
        return parts[-2] == self.CLASS_NAMES

    def decode_img(self, img: tf.Tensor) -> tf.Tensor:
        # convert the compressed string to a 3D uint8 tensor
        img = tf.image.decode_jpeg(img, channels=3)
        # Use `convert_image_dtype` to convert to floats in the [0,1] range.
        return tf.image.convert_image_dtype(img, tf.float32)

    def process_path(self, file_path: str) -> typing.Tuple[tf.Tensor, str]:
        label = self.get_label(file_path)
        # load the raw data from the file as a string
        img: tf.Tensor = tf.io.read_file(file_path)
        img = self.decode_img(img)
        return img, label

    def load_data(self) -> typing.Tuple[tf.data.Dataset, typing.List[str]]:
        return (
            self.list_ds.map(self.process_path, num_parallel_calls=AUTOTUNE),
            self.CLASS_NAMES,
        )
