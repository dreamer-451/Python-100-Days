"""
question：设计一个函数返回传入的列表中最大和第二大的元素的值
author：吕梦龙
date：2023-09-07
"""
def max2(nums):
    nums.sort(reverse = True)
    return nums[0], nums[1]

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_1, num_2 = max2(nums)
    print(num_1, num_2)
