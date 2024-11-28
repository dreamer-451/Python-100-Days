"""
question：在屏幕上显示跑马灯文字
author：吕梦龙
date：2023-09-07
"""

if __name__ == '__main__':
    msg = input("message: ")
    while True:
        print(msg)
        msg = msg[1:] + msg[0]
