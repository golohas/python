# codgin=utf-8

import cProfile
import sys
import os
import time
import psutil
from configparser import ConfigParser


def fun():
    a = 0
    b = 0
    for i in range(100000):
        a = a+i*i
    for i in range(3):
        b += 1
    time.sleep(0.1)
    return a+b


def get_mem_info():
    mem = psutil.virtual_memory()
    mem1 = str(mem.total/1024/1024/1024)
    print("total mem: ", mem1[0:4], " G")


def get_path():
    script_path = sys.argv[0]
    full_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    print(script_path)
    print(full_path)


if __name__ == "__main__":

<<<<<<< HEAD
    # cProfile.run('fun()')
    get_path()
=======
    cProfile.run('fun()') // TODO @ xjzhao
>>>>>>> 614717edd95ec003f1e367d9ec4d10f6425c0ee1
