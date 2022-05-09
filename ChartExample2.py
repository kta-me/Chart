import matplotlib.pyplot as plt
import numpy as np

def plot_chart():
    mean = 0
    sigma = 1
    x = np.arange(-5, 5, .01)
    f = np.exp(-np.square((x-mean)/sigma)/2)/(np.sqrt(2*np.pi)*sigma)

    fig, ax = plt.subplots()
    ax.plot(x, f)

    ax.set(xlabel='X', ylabel='Y', title='Нормальное распледение')
    ax.grid()

    plt.show()
