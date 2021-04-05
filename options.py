import numpy as np
import matplotlib.pyplot as plt

def call(stock, strike, premium):
    return max(stock-strike, 0)-premium

def put(stock, strike, premium):
    return max(strike-stock, 0)-premium

def test_output():
    x = list(np.arange(0, 10, 0.1))
    y = list(map(lambda elem: call(elem, 5, 1), x))
    y2 = list(map(lambda elem: put(elem, 5, 1), x))
    y3 = [i+j for i,j in zip(y, y2)]

    plt.plot(x, y)
    plt.show()
    plt.plot(x, y2)
    plt.show()
    plt.plot(x,y3)
    plt.show()

    x = np.arange(0, 80, 0.25)
    y1 = np.asarray(list(map(lambda elem: call(elem, 30, 0), x)))
    y2 = np.asarray(list(map(lambda elem: call(elem, 35, 0), x)))
    y3 = np.asarray(list(map(lambda elem: call(elem, 40, 0), x)))
    y4 = np.asarray(list(map(lambda elem: put(elem, 20, 0), x)))
    y5 = np.asarray(list(map(lambda elem: put(elem, 15, 0), x)))
    y = y1 + (-2*y2) + y3

    plt.plot(x, y)
    plt.title('Butterfly spread')
    plt.show()
    plt.plot(x, y1-y2)
    plt.title('Bull spread')
    plt.show()
    plt.plot(x, y4-y5)
    plt.title('Bear spread')
    plt.show()

    y1 = np.asarray(list(map(lambda elem: call(elem, 45, 4), x)))
    y2 = np.asarray(list(map(lambda elem: call(elem, 50, 6), x)))
    y3 = np.asarray(list(map(lambda elem: call(elem, 55, 9), x)))

    plt.axhline(y=0, color='r')
    plt.axvline(x=46, color='r')
    plt.axvline(x=54, color='r')
    plt.plot(x, y1+y3+(-2*y2))
    plt.show()
