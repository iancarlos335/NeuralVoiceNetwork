import sys
import numpy as np
import matplotlib

inputs = [1, 2, 3, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, -0.26, 0.5],
    [-0.26, -0.27, 0.17, 0.87]
]

bias1 = 2
bias2 = 3
bias3 = 0.5

biases = [2, 3, 0.5]

some_value = -0.5
weigh = 0.7
bias = 0.7

print(some_value*weigh)
print(some_value+bias)

'''
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weights in zip(inputs, neuron_weights):
        neuron_output += n_input*weights
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
'''
