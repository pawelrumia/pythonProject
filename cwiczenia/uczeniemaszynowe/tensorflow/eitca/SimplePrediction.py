import tensorflow as tf
import tensorflow_datasets as tfds

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

sample_data = [[5.1, 3.3, 1.7, 0.5]]  # Or replace this with your data
predictions = model.predict(sample_data)
predicted_class = tf.argmax(predictions, axis=1).numpy()
print(f"Predicted class: {predicted_class}")