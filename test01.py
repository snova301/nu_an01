# -*- coding: utf-8 -*- #


import time
start = time.time()

import numpy as np
# import matplotlib.pyplot as plt
import os
import shutil
import sys


def main():
    np_a = np.array([1, 2])
    np_b = np.sin(np_a)
    print(np_a)
    print(np_b)


if __name__ == '__main__':
    main()

    # --- Record Time --- #
    time = time.time() - start
    print(('Time : {0}'.format(time)) + ' [sec]')
