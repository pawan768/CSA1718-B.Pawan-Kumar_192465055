# Feed-forward neural network for handwritten digit image classification
# Install: pip install tensorflow
import tensorflow as tf
from tensorflow.keras import layers, models

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

model = models.Sequential([
    layers.Input(shape=(28, 28)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])
model.fit(x_train, y_train, epochs=3, batch_size=64, validation_split=0.1)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print("Test accuracy:", round(accuracy * 100, 2), "%")
print("First test image predicted digit:", model.predict(x_test[:1], verbose=0).argmax())
