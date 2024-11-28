"""
question：华氏温度转换为摄氏温度
author：吕梦龙
date：2023-09-04
"""

def trans_cf(c):
    f = c * 1.8 + 32
    return f

def trans_fc(f):
    c = (f - 32) / 1.8
    return c

if __name__ == '__main__':
    c = float(input("Please input the Celsius degree:"))
    c_f = trans_cf(c)
    print(f"The Fahrenheit degree is {c_f}.")
    f = float(input("Please input the Fahrenheit degree:"))
    f_c = trans_fc(f)
    print(f"The Celsius degree is {f_c}.")
