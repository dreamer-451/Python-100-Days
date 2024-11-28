"""
question：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
author：吕梦龙
date：2023-09-07
"""
import random

def check(length, chars):
    checkstr = random.sample(chars, length)
    checkstr = "".join(checkstr)
    return checkstr

if __name__ == '__main__':
    length = int(input("length: "))
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    checkstr = check(length, chars)
    print(checkstr)
