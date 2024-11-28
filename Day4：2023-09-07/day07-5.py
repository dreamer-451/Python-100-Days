"""
question：计算指定的年月日是这一年的第几天
author：吕梦龙
date：2023-09-07
"""
def dayOfYear(year, month, day):
    dayOfMonth = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if year % 4 == 0 and year % 100 != 0:
        isLeap = 1
    elif year % 400 == 0:
        isLeap = 1
    else:
        isLeap = 0
    if month >= 3 and isLeap == 1:
        days = 1
    else:
        days = 0
    for i in range(1, month):
        days += dayOfMonth[i]
    days += day
    return days


if __name__ == '__main__':
    year = int(input("year: "))
    month = int(input("month: "))
    day = int(input("day: "))
    print(dayOfYear(year, month, day))
