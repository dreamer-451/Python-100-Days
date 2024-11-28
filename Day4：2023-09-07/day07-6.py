"""
question：打印杨辉三角
author：吕梦龙
date：2023-09-07
"""
def generate(numRows):
    yh_tri = [[] for i in range(numRows)]
    match numRows:
        case 1:
            yh_tri[0] = [1]
        case 2:
            yh_tri[0] = [1]
            yh_tri[1] = [1, 1]
        case _:
            yh_tri[0] = [1]
            yh_tri[1] = [1, 1]
            for i in range(2, numRows):
                yh_tri[i].append(1)
                for j in range(i - 1):
                    yh_tri[i].append(yh_tri[i - 1][j] + yh_tri[i - 1][j + 1])
                yh_tri[i].append(1)
    return yh_tri

if __name__ == '__main__':
    numRows = int(input("row: "))
    yh = generate(numRows)
    for tri in yh:
        print(tri)
