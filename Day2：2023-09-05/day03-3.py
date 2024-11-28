"""
question：输入三条边长，如果能构成三角形就计算周长和面积
author：吕梦龙
date：2023-09-05
"""
import math

if __name__ == '__main__':
    a = float(input("Please input a:"))
    b = float(input("Please input b:"))
    c = float(input("Please input c:"))
    if a + b > c and b + c > a and c + a > b:
        perimeter = a + b + c
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"perimeter = {perimeter}, area = {area}")
    else:
        print("cannot to be a triangle")
