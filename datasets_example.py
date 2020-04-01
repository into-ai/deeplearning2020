from deeplearning2020.datasets import ImageWoof

train_data, test_data, classes = ImageWoof.load_data()

print(f"Classes: ", classes)

for sample in train_data.take(1):  # Only take a single example
    image, label = sample
    print(image, label)
