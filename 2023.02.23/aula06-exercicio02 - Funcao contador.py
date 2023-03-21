
"""
Created on 23/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import time

def contador(__start, __stop, __step=1, __time=0):
    if __start < __stop:
        while __start < __stop:
            time.sleep(__time)
            print("{:.2f}".format(__start).rstrip("0").rstrip("."))
            __start += __step
    elif __start > __stop:
        while __start > __stop:
            time.sleep(__time)
            print("{:.2f}".format(__start).rstrip("0").rstrip("."))
            __start += __step

_start = float(input('valor inicial: '))
_stop = float(input('valor final: '))
_step = float(input('valor de passo: '))
_time = float(input('tempo a cada passo: '))

contador(_start, _stop, _step, _time)