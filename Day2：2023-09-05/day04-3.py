"""
question：打印三角形图案
author：吕梦龙
date：2023-09-05
"""

if __name__ == '__main__':
    line = int(input("The triangle's line: "))
    print("left triangle:")
    for i in range(line):
        print("*" * (i + 1))
    print("right triangle:")
    for i in range(line):
        print(" " * (line - i - 1) + "*" * (i + 1))
    print("middle triangle:")
    for i in range(line):
        print(" " * (line - i - 1) + "*" * (2 * i + 1))
