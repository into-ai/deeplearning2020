from __future__ import absolute_import, division, print_function, unicode_literals

import os
import pathlib
import typing
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:  # pragma: no cover
    import tensorflow as _tf

try:
    import tensorflow as tf

    assert tf.__version__[:2] == "2."
except ImportError:
    raise ImportError(
        'Das Dataset erfordert tensorflow 2! Lokal geht das mit "conda install tensorflow>=2.0.0" oder "pip install tensorflow>=2.0.0"'
    )
except AssertionError:
    raise ImportError(
        'Das Dataset erfordert tensorflow 2! In Colab kannst du dies mit dem "%tensorflow_version 2.x" Befehl erzwingen. Anschliessend musst du die Runtime restarten. Schaue dir dazu am Besten nochmal die Beispiel Notebooks aus dieser Woche an!'
    )

AUTOTUNE = tf.data.experimental.AUTOTUNE

"""
The imagewoof dataset is provided by FastAI

author    = "Jeremy Howard",
title     = "imagenette",
url       = "https://github.com/fastai/imagenette/"
"""


ImageWoofType = typing.TypeVar("ImageWoofType", bound="ImageWoof")


class ImageWoof:
    BATCH_SIZE: int = 32
    CLASS_NAMES: np.ndarray = None
    data_dir: pathlib.Path
    image_count: int = 0
    list_ds: "_tf.data.Dataset" = None

    def __init__(self, dataset: str) -> None:
        if dataset not in ["train", "val"]:
            raise ValueError("Dataset not found")

        file_path = tf.keras.utils.get_file(
            origin="https://s3.amazonaws.com/fast-ai-imageclas/imagewoof2-320.tgz",
            fname="imagewoof",
            untar=True,
        )
        self.data_dir = pathlib.Path(file_path + "2-320/" + dataset)
        print(self.data_dir)
        self.image_count = len(list(self.data_dir.glob("*/*.JPEG")))
        print(f"Loaded {self.image_count} images")

        self.raw_class_names = [
            item.name for item in self.data_dir.glob("*") if item.name != "LICENSE.txt"
        ]

        self.class_name_mapping = dict(
            n02096294="Australian terrier",
            n02093754="Border terrier",
            n02111889="Samoyed",
            n02088364="Beagle",
            n02086240="Shih-Tzu",
            n02089973="English foxhound",
            n02087394="Rhodesian ridgeback",
            n02115641="Dingo",
            n02099601="Golden retriever",
            n02105641="Old English sheepdog",
        )

        self.CLASS_NAMES = np.array([self.map_class(c) for c in self.raw_class_names])
        self.list_ds = tf.data.Dataset.list_files(str(self.data_dir / "*/*"))

    @classmethod
    def train(cls: typing.Type[ImageWoofType]) -> ImageWoofType:
        return cls("train")

    @classmethod
    def validation(cls: typing.Type[ImageWoofType]) -> ImageWoofType:
        return cls("val")

    def map_class(self, raw_cls: str) -> str:
        return self.class_name_mapping[raw_cls]

    def get_label(self, file_path: str) -> "_tf.Tensor":
        # convert the path to a list of path components
        parts = tf.strings.split(file_path, os.path.sep)
        # The second to last is the class-directory
        label = parts[-2] == self.raw_class_names
        label = tf.reduce_sum(tf.where(label))
        return label

    def decode_img(self, img: "_tf.Tensor") -> "_tf.Tensor":
        # convert the compressed string to a 3D uint8 tensor
        img = tf.image.decode_jpeg(img, channels=3)
        # Use `convert_image_dtype` to convert to floats in the [0,1] range.
        return tf.image.convert_image_dtype(img, tf.float32)

    def process_path(self, file_path: str) -> typing.Tuple["_tf.Tensor", str]:
        label = self.get_label(file_path)
        # load the raw data from the file as a string
        img: "_tf.Tensor" = tf.io.read_file(file_path)
        img = self.decode_img(img)
        return img, label

    def wrapped_load_data(self) -> "_tf.data.Dataset":
        return self.list_ds.map(self.process_path, num_parallel_calls=AUTOTUNE)

    @classmethod
    def load_data(
        cls: typing.Type[ImageWoofType],
    ) -> typing.Tuple["_tf.data.Dataset", "_tf.data.Dataset", np.ndarray]:
        train_ds = cls.train()
        return (
            train_ds.wrapped_load_data(),
            cls.validation().wrapped_load_data(),
            train_ds.CLASS_NAMES,
        )
