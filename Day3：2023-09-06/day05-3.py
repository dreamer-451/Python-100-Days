"""
question：输出100以内所有的素数
author：吕梦龙
date：2023-09-06
"""

if __name__ == '__main__':
    n = 100
    primeNum = [0, 0] + [1] * (n - 2)
    for i in range(2, n):
        if i * i < n:
            for j in range(i * i, n, i):
                primeNum[j] = 0
    ans = []
    for i in range(n):
        if primeNum[i] == 1:
            ans.append(i)
    print(ans)
