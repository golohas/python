# codgin=utf-8

import cProfile
import time


def fun():
    a = 0
    b = 0
    for i in range(100000):
        a = a+i*i
    for i in range(3):
        b += 1
    time.sleep(0.1)
    return a+b


if __name__ == "__main__":

    cProfile.run('fun()') // TODO @ xjzhao
