"""
question：百分制成绩转换为等级制成绩
author：吕梦龙
date：2023-09-05
"""
def trans(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    return grade

if __name__ == '__main__':
    score = float(input('score: '))
    grade = trans(score)
    print(f'grade: {grade}')