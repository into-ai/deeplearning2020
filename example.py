from tensorflow import keras
from deeplearning2020 import Submission

data = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

total_classes = 10
train_vec_labels = keras.utils.to_categorical(train_labels, total_classes)
test_vec_labels = keras.utils.to_categorical(test_labels, total_classes)

model = keras.Sequential(
    [
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation="sigmoid"),
        keras.layers.Dense(10, activation="sigmoid"),
    ]
)

model.compile(optimizer="sgd", loss="mean_squared_error", metrics=["accuracy"])

model.fit(train_images, train_vec_labels, epochs=2, verbose=True)

eval_loss, eval_accuracy = model.evaluate(test_images, test_vec_labels, verbose=False)
print("Model accuracy: %.2f" % eval_accuracy)

Submission(
    user_token="<your-token>", assignment_id=2, model=model
).submit()
