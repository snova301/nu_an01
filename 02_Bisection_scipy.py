# -*- coding: utf-8 -*- #

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

def main():
    min_x = 2
    max_x = 5
    x = np.linspace(min_x, max_x, 100)
    y = func_y(x)

    ans_x = bisect(func_y, min_x, max_x)
    ans_y = func_y(ans_x)
    print('x : '+str(ans_x))
    print('y : '+str(ans_y))

    plt.plot(x, y, color='b', label='function')
    plt.plot(ans_x, ans_y, 'o', color='r', label='solution')
    plt.legend()
    plt.savefig('fig02.png')
    # plt.show()


def func_y(x_dat):
    func = 2*x_dat**2 - 3*x_dat - 4
    return func

if __name__ == '__main__':
    main()
