# -*- coding: utf-8 -*- #

import numpy as np
import matplotlib.pyplot as plt

def main():
    init_val = 4.0
    delta_val = 0.0001
    min_x = -5
    max_x = 5
    x = np.linspace(min_x, max_x, 100)
    y = func_y(x)

    for i in range(50):
        f = func_y(init_val)
        df = (func_y(init_val + delta_val) - func_y(init_val)) / delta_val
        init_val = init_val - f/df

    ans_x = init_val
    ans_y = func_y(ans_x)
    print('x : '+str(ans_x))
    print('y : '+str(ans_y))

    plt.plot(x, y, color='b', label='function')
    plt.plot(ans_x, ans_y, 'o', color='r', label='solution')
    plt.legend()
    plt.savefig('fig03.png')
    # plt.show()


def func_y(x_dat):
    func = 2*(x_dat**2) - 3*x_dat - 4
    return func

if __name__ == '__main__':
    main()
