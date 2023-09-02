
#   [2.0, 2.4, 1.5, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7]
#    [196, 221, 136, 255, 244, 230, 232, 255, 267]
#    tim con so ung voi gia tri 2.4 (Simple Linear Regression)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clor

def Linear_Regress(x: np.ndarray, y: np.ndarray) -> list:
    a = np.mean(x)
    b = np.mean(y)

    SSxy = np.sum((x-a) * (y-b))
    SSxx = np.sum((x-a) ** 2)
    # print("SSxy and SSxx is:", SSxy, SSxx)
    b_1 = SSxy / SSxx
    b_0 = b - b_1 * a

    return b_0, b_1

def plot_resg(x: np.ndarray, y: np.ndarray, b: list):
    y_pred = b[0] + x * b[1]
    plt.scatter(x, y)
    plt.plot(x, y_pred, color="k", linewidth=1)

    plt.title("Simple Linear Regression")
    plt.xlabel("Income")
    plt.ylabel("happiness")
    plt.show()

def main():
    X = [1,2,3,4,5,6]
    Y = [10,12,14, 16,18, 20]
    x = np.array(X)
    y = np.array(Y)
    b = Linear_Regress(x, y)
    print('b0: {} - b1: {}'.format(b[0], b[1]))

if __name__ == "__main__":
    # nhung gi trong nay se duoc thuc thi dau tien
    # trong file object __name__ se luon la __main__
    main() 