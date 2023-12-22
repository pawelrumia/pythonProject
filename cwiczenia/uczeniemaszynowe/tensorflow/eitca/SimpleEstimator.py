import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

#load dataset
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target.reshape(-1, 1), random_state=42)
# One hot encode target values
enc = OneHotEncoder(sparse=False)
y_train_onehot = enc.fit_transform(y_train)
y_test_onehot = enc.transform(y_test)

data = iris
train_data = iris
test_data = iris

def preprocess(dataset):
    def _preprocess_img(image, label):
        label = tf.one_hot(label, depth=3)
        return image, label
    dataset = dataset.map(_preprocess_img)
    return dataset.batch(32).prefetch(tf.data.experimental.AUTOTUNE)

# Build a simple neural network model
# model = tf.keras.models.Sequential([
# tf.keras.layers.Dense(10, input_shape=(4,), activation='relu'),
# tf.keras.layers.Dense(3, activation='softmax')
# ])

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train_onehot, epochs=100, validation_data=(X_test, y_test_onehot))

loss, accuracy = model.evaluate(X_test, y_test_onehot)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")

#save model
model.save("my_model")
