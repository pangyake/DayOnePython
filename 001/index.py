# -*- coding: utf-8 -*-
# @Time    : 2017/9/15 下午6:16
# @Author  : Yaker
# @Email   : 499851260@qq.com
# @File    : index.py
# @Software: PyCharm Community Edition
sum = 0
for a in range(1,6):
    for b in range(1,6):
        for c in range(1,6):
            for d in range(1,6):
                if a != b and a != c and a != d and b != c and b != d and c !=d:
                    sum += 1
                    print(1000*a +100*b +10*c +d)

print(sum)