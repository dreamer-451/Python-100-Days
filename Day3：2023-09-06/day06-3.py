"""
question：实现判断一个数是不是素数的函数
author：吕梦龙
date：2023-09-06
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
