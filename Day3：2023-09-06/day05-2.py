"""
question：找出10000以内的完美数
author：吕梦龙
date：2023-09-06
"""

if __name__ == '__main__':
    ans = []
    for i in range(2, 10000):
        temp = [1]
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                temp.extend([j, i % j])
        if sum(temp) == i:
            ans.append(i)
    print(ans)
