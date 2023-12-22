import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

m = 2
b = 0.11
x = np.linspace(0, 4, 100)

y = (m * x) + b + np.random.randn(*x.shape) + 0.1
# plt.scatter(x, y)
# plt.show()


class RegressionModel:
    def __init__(self):
        self.weight = tf.Variable(10.0);
        self.bias = tf.Variable(10.0)

    def __call__(self, x):
        return (self.weight * x) + self.bias


def calculate_loss(y_actual, x_actual):
    return tf.reduce_mean(tf.square(y_actual - x_actual))


def train_function(model, x, y_expected, learning_rate):
    with tf.GradientTape() as gt:
        y_output = model(x)
        loss = calculate_loss(y_output, y_expected)

    new_weight, new_bias = gt.gradient(loss, [model.weight, model.bias])
    model.weight.assign_sub(new_weight * learning_rate)
    model.bias.assign_sub(new_bias * learning_rate)


model = RegressionModel()
epochs = 100
learning_rate = 0.15
current_epochs = []
losses = []
for epoch in range(epochs):
    y_output = model(x)
    loss = calculate_loss(y_output, y)
    print(f"Epoch: {epoch}, loss: {loss.numpy()}")
    current_epochs.append(epoch)
    losses.append(loss)
    train_function(model, x, y, learning_rate)
# plt.plot(current_epochs, losses)
# plt.show()

new_m = model.weight.numpy()
new_b = model.bias.numpy()
print(new_m)
print(new_b)

new_y = (new_m * x) + new_b
plt.scatter(x,y)
plt.scatter(x, new_y)
plt.show()
