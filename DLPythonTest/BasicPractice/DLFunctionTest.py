#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数就是最基本的一种代码抽象方式
# abs(1,2) #报错，多了一个参数
# abs('a') #报错，参数类型错误
print(hex(10))


#定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

#函数导入
# from DLFunctionTest import my_abs  #导入函数

