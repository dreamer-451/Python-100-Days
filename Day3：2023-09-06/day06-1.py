"""
question：实现计算求最大公约数和最小公倍数的函数
author：吕梦龙
date：2023-09-06
"""
def gcd(x, y):
    if x == y:
        return x
    elif max(x, y) % min(x, y) == 0:
        return min(x, y)
    else:
        for i in range(min(x, y) // 2, 0, -1):
            if x % i == 0 and y % i == 0:
                 return i

def lcm(x, y):
    if x == y:
        return x
    elif max(x, y) % min(x, y) == 0:
        return max(x, y)
    else:
        return x * y // gcd(x, y)

if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"gcd: {gcd(a, b)} and lcm: {lcm(a, b)}")