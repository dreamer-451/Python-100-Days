"""
question：输入一个正整数判断是不是素数
author：吕梦龙
date：2023-09-05
"""
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    num = int(input("num: "))
    print(isPrime(num))

