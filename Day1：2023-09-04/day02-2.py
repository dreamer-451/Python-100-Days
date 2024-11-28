"""
question：输入圆的半径计算计算周长和面积
author：吕梦龙
date：2023-09-04
"""
import math

if __name__ == '__main__':
    radius = float(input('Please input the radius of circle:'))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print(f'perimeter: {perimeter}')
    print(f'area: {area}')
