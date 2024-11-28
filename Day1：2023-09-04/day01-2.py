"""
question：学习使用turtle在屏幕上绘制图形
author：吕梦龙
date：2023-09-04
"""
from turtle import *

def taiji():
    # 整体范围限定
    circle(200)

    # 黑色阴鱼填充
    fillcolor("black")
    begin_fill()
    circle(200, 180)
    circle(100, 180)
    end_fill()

    #白色阳鱼修订
    fillcolor("white")
    begin_fill()
    circle(-100, 180)
    end_fill()

    # 阳鱼眼绘制
    up()
    circle(-25,-180)
    down()
    fillcolor("black")
    begin_fill()
    circle(50)
    end_fill()

    # 阴鱼眼绘制
    up()
    circle(100,180)
    down()
    fillcolor('white')
    begin_fill()
    circle(-50)
    end_fill()

    done()

if __name__ == '__main__':
    taiji()
