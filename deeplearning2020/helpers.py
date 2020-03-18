import typing
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

if TYPE_CHECKING:  # pragma: no cover
    import keras.models
    from tf.keras.callbacks import History
    from tf.python.data.ops.dataset_ops import DatasetV1Adapter


def plot_predictions(
    mdl: "keras.models.Model",
    imgs: np.ndarray,
    labels: typing.Optional[np.ndarray] = None,
    classes: typing.Optional[typing.List[int]] = None,
    max_cols: int = 3,
    figsize: typing.Tuple[int, int] = (3, 2),
) -> None:
    assert len(imgs) > 0, "Need at least one input"
    if labels is not None:
        assert len(imgs) == len(labels), "Need as many labels as inputs!"
    num_cols = min(len(imgs), max_cols)
    num_rows = int(len(imgs) / num_cols)
    fig, plots = plt.subplots(
        num_rows, num_cols, figsize=(figsize[0] * num_cols, figsize[1] * num_rows)
    )
    model_predictions = mdl.predict(imgs)
    if classes is None:
        classes = list(range(len(model_predictions[0])))
    else:
        assert len(classes) == len(
            model_predictions[0]
        ), "Need as many classes as there are output neurons"
    for r in range(num_rows):
        for c in range(num_cols):
            i = r * num_cols + c
            if not i < len(imgs):
                continue
            predicted_label = classes[np.argmax(model_predictions[i])]
            if labels is None:
                color = "blue"
            else:
                color = "green" if predicted_label == np.argmax(labels[i]) else "red"
            plots[r][c].tick_params(top=False, bottom=False, left=False, right=False)
            plots[r][c].imshow(imgs[i], cmap=plt.cm.binary)
            plots[r][c].axis("off")
            plots[r][c].set_title(
                "Predicted {}".format(predicted_label), color=color,
            )


def plot_worst(
    mdl: "keras.models.Model",
    imgs: np.ndarray,
    labels: np.ndarray,
    classes: typing.Optional[typing.List[int]] = None,
    num: int = 9,
    max_cols: int = 3,
    figsize: typing.Tuple[int, int] = (3, 2),
) -> None:
    assert len(imgs) > 0, "Need at least one input"
    assert len(imgs) == len(labels), "Need as many labels as inputs!"
    max_imgs = min(num + 1, len(imgs))
    pred = mdl.predict(imgs)
    i = 0
    wrong_imgs = np.expand_dims(np.ndarray(shape=imgs[0].shape), axis=0)
    wrong_labels = np.expand_dims(np.ndarray(shape=labels[0].shape), axis=0)
    while len(wrong_imgs) < max_imgs and i < len(imgs):
        if np.argmax(pred[i]) != np.argmax(labels[i]):
            wrong_imgs = np.append(wrong_imgs, np.expand_dims(imgs[i], axis=0), axis=0)
            wrong_labels = np.append(
                wrong_labels, np.expand_dims(labels[i], axis=0), axis=0
            )
        i += 1
    plot_predictions(
        mdl,
        wrong_imgs[1:],
        wrong_labels[1:],
        classes=classes,
        max_cols=max_cols,
        figsize=figsize,
    )


def plot_learning_curve(
    title: str, x: int, y: int, y_test: int, ylim: float = 0.6
) -> None:
    plt.figure()
    plt.title(title)
    axes = plt.gca()
    axes.set_ylim([ylim, 1])
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    train_sizes = x
    train_scores = y
    test_scores = y_test

    plt.grid()

    plt.plot(
        train_sizes,
        train_scores,
        "o-",
        color=(177 / 255, 6 / 255, 58 / 255),
        label="Training accuracy",
    )
    plt.plot(
        train_sizes,
        test_scores,
        "o-",
        color=(246 / 255, 168 / 255, 0),
        label="Validation accuracy",
    )

    plt.legend(loc="best")


def plot_history(title: str, history: "History", ylim: float = 0.6) -> None:
    y = history.history["accuracy"]
    y_test = history.history["val_accuracy"]
    plot_learning_curve(title, np.arange(1, 1 + len(y)), y, y_test, ylim)


def plot_two_histories(history: "History", history_finetune: "History") -> None:
    y = history.history["accuracy"] + history_finetune.history["accuracy"]
    y_test = history.history["val_accuracy"] + history_finetune.history["val_accuracy"]
    plot_learning_curve("Transfer Learning", np.arange(1, 1 + len(y)), y, y_test, 0)


def plot_images(images: "DatasetV1Adapter", class_names: typing.List[str]) -> None:
    plt.figure(figsize=(12, 10))
    index = 0
    for image, label in images:
        index += 1
        plt.subplot(3, 3, index)
        plt.imshow(image)
        plt.title("Class: {}".format(class_names[label]))
        plt.axis("off")


def plot_images_with_labels(
    images: typing.List[int], labels: np.ndarray, class_names: typing.List[str]
) -> None:
    if len(images) != 9:
        images = images[:9]
        labels = labels[:9]
    labels = labels.astype("int")

    plt.figure(figsize=(12, 10))
    index = 0
    for image, label in zip(images, labels):
        index += 1
        plt.subplot(3, 3, index)
        plt.imshow(image)
        plt.title("Class: {}".format(class_names[label]))
        plt.axis("off")


def preprocess(
    image: typing.Any, label: typing.Any
) -> typing.Tuple[typing.Any, typing.Any]:
    """ resize the images to a uniform size """
    resized_image = tf.image.resize(image, [224, 224])
    # run Xceptions preprocessing function
    preprocessed_image = tf.keras.applications.xception.preprocess_input(resized_image)
    return preprocessed_image, label


def dataset_to_ndarray(
    train_data: "DatasetV1Adapter", test_data: "DatasetV1Adapter"
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # convert tf.Dataset in np.ndarray, because ImageDataGenerators for
    # data augmentation don't work with tf.Datasets
    preprocessed_train_data = train_data.map(preprocess).batch(2950)
    preprocessed_test_data = test_data.map(preprocess).batch(720)

    x = np.array([])
    y = np.array([])
    for elem in preprocessed_train_data:
        x = np.append(x, elem[0].numpy())
        y = np.append(y, elem[1].numpy())

    x_test = np.array([])
    y_test = np.array([])
    for elem in preprocessed_test_data:
        x_test = np.append(x_test, elem[0].numpy())
        y_test = np.append(y_test, elem[1].numpy())

    # X was flat before
    x = x.reshape(len(x) // (224 * 224 * 3), 224, 224, 3)
    x_test = x_test.reshape(len(x_test) // (224 * 224 * 3), 224, 224, 3)
    return x, y, x_test, y_test
