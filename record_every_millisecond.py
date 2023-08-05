"""
File: record_every_millisecond.py
Author: Chuncheng Zhang
Date: 2023-08-04
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-08-04 ------------------------
# Requirements and constants
import time
import random
import threading

# from rich import print
from loguru import logger as LOGGER

# %%
LOGGER.add('log/mylog.log')


# %% ---- 2023-08-04 ------------------------
# Function and class
class DataRecorder(object):
    sample_interval = 1  # milliseconds
    inv_1000 = 1 / 1000

    def __init__(self):
        self.reset()
        LOGGER.debug('Initialized {}'.format(self.__class__))

    def fetch_serial(self):
        return [random.random(), random.random(), random.random()]

    def peek(self, latest_index=20):
        return self.data[-latest_index:]

    def reset(self):
        self.data = []
        self.n = 0
        self.running_flag = True
        LOGGER.debug('Reset')

    def run_forever(self):
        self.reset()
        threading.Thread(target=self._loop, daemon=True).start()
        LOGGER.debug('Started run_forever')

    def _loop(self):
        tic = time.time()
        while self.running_flag:
            t = time.time()
            d = t - tic
            if d >= (self.n * self.sample_interval * self.inv_1000):
                self.data.append((self.fetch_serial(), d, t))
                self.n += 1
            else:
                continue
            pass

        LOGGER.debug('Finished run_forever loop')


# %% ---- 2023-08-04 ------------------------
# Play ground
if __name__ == "__main__":
    dr = DataRecorder()
    dr.run_forever()

    while True:
        inp = input('>>')
        if inp == 'q':
            break

        print('------------------------------')
        d = dr.peek()
        for j, row in enumerate(d):
            if j > 0:
                print('{:04d}-{:0.3f}-{}'.format(j, row[-1] - d[j-1][-1], row))
            else:
                print('{:04d}-{:0.3f}-{}'.format(j, row[-1] - d[j][-1], row))

    print('Bye.')


# %% ---- 2023-08-04 ------------------------
# Pending


# %% ---- 2023-08-04 ------------------------
# Pending
