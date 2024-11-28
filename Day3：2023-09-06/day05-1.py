"""
question：生成斐波那契数列的前20个数
author：吕梦龙
date：2023-09-06
"""

if __name__ == '__main__':
    fib = [0, 1]
    for i in range(2, 20):
        fib.append(fib[i - 1] + fib[i - 2])
    print(fib)
