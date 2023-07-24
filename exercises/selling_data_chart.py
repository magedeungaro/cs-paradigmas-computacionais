# run on jupiter notebook https://colab.research.google.com/drive/1RicMATZUmR-9fV7je6G50QUUGeKAh9VD?usp=sharing

import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series;
import matplotlib.pyplot as plt;

def generate_data():
    x_axis = np.array(['A', 'B', 'C', 'D']);
    y_axis = np.array([3, 8, 1, 10]);
    return x_axis, y_axis;

def plot_data(x_axis, y_axis):
    plt.bar(x_axis, y_axis, color = 'red');
    plt.show();

def main():
    x_axis, y_axis = generate_data();
    plot_data(x_axis, y_axis);


main();