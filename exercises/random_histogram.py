# run on google collab https://colab.research.google.com/drive/1UdQFOBw-pJIm_5amId9ZJ3VSyV4bRisV?usp=sharing

import numpy as np;
import matplotlib.pyplot as plt;

def generate_data():
    return np.random.normal(20, 2, 1000);

def plot_data(data):
    plt.hist(data);
    plt.show();

def main():
    data = generate_data();
    plot_data(data);

main();