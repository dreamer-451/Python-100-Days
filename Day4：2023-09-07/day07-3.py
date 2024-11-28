"""
question：设计一个函数返回给定文件名的后缀名
author：吕梦龙
date：2023-09-07
"""
def suffix(filename):
    if '.' not in filename:
        return ''
    strs = filename.split('.')
    return strs[-1]

if __name__ == '__main__':
    filename = input("filename: ")
    print(suffix(filename))
