"""
question：输入年份判断是不是闰年
author：吕梦龙
date：2023-09-04
"""

if __name__ == '__main__':
    year = int(input("Please the year number:"))
    if year % 4 == 0 and year % 100 != 0:
        isLeap = True
    elif year % 400 == 0:
        isLeap = True
    else:
        isLeap = False
    print(isLeap)
