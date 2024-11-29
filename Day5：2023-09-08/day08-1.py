"""
question：定义一个类描述数字时钟
author：吕梦龙
date：2023-09-08
"""
from time import sleep


class Clock:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def go(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def show(self):
        return f"{self.hour}:{self.minute}:{self.second}"

if __name__ == '__main__':
    clock = Clock()
    while True:
        print(clock.show())
        clock.go()
        sleep(1)
