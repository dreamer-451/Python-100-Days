"""
question：写一个程序判断输入的正整数是不是回文素数
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

def isPalindrome(num):
    num0 = num
    num1 = 0
    while num0 > 0:
        num1 = num1 * 10 + num0 % 10
        num0 //= 10
    return num == num1

if __name__ == '__main__':
    num = int(input("num: "))
    if isPalindrome(num):
        print(isPrime(num))
    else:
        print(isPalindrome(num))
