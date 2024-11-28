"""
question：英制单位英寸与公制单位厘米互换
author：吕梦龙
date：2023-09-05
"""

if __name__ == '__main__':
    length = input("Please input length (in or cm):")
    match length[-2:]:
        case "in":
            ans = str(float(length[:-2]) * 2.54) + "cm"
        case "cm":
            ans = str(float(length[:-2]) / 2.54) + "in"
        case _:
            ans = "Unexpected unit."
    print(ans)
