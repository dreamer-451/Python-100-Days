"""
question：实现判断一个数是不是回文数的函数
author：吕梦龙
date：2023-09-06
"""
def isPalindrome(num):
    num0 = num
    num1 = 0
    while num0 > 0:
        num1 = num1 * 10 + num0 % 10
        num0 //= 10
    return num == num1

if __name__ == '__main__':
    num = int(input("num: "))
    print(isPalindrome(num))
