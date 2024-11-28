"""
question：输入两个正整数，计算它们的最大公约数和最小公倍数
author：吕梦龙
date：2023-09-05
"""

if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))
    if a == b:
        gcd = a
        lcm = a
    elif max(a, b) % min(a, b) == 0:
        gcd = min(a, b)
        lcm = max(a, b)
    else:
        for i in range(min(a, b) // 2, 0, -1):
            if a % i == 0 and b % i == 0:
                gcd = i
                break
        lcm = gcd * (a // gcd) * (b // gcd)
    print(f"gcd: {gcd} and lcm: {lcm}")
