#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数就是最基本的一种代码抽象方式
# abs(1,2) #报错，多了一个参数
# abs('a') #报错，参数类型错误
print(hex(10))


#定义函数
def my_abs(x):
    #参宿检查
    if not isinstance(x,(int,float)):
        raise  TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

#函数导入
# from DLFunctionTest import my_abs  #导入函数

#空函数 什么都不做的函数
def nop():
    pass  #用来干什么，用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来


# my_abs('A')


#返回多个值
import math
def move(x,y,step,angle=0): #作用：在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny


x,y = move(100,100,60,math.pi / 6)

print(x,y)

def quadratic(a,b,c):
    p = b*b - 4*a*c
    if p >= 0 and a != 0:#一元二次方程有解得条件
        x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
        return x1,x2
    elif a==0:#一元一次方程
        x1=x2=-c/b
        return x1
    else:
        return('Wrong Number!')

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2,3,1) != (-0.5,-1.0):
    print("测试失败")
elif quadratic(1,3,-4) != (1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')

#函数的参数
#1.未知参数
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2))
# 设置默认参数时，有几点要注意：
#
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#
# 二是如何设置默认参数。
#
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def enroll(name,gender,age=6, city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')

def add_end_wrong(L=[]):  #定义默认参数要牢记一点：默认参数必须指向不变对象
    L.append('END')
    return L

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


add_end([1,2,3])
add_end(['x','y','z'])


add_end()
add_end()
add_end()
print(add_end())


#可变参数
def calc_original(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc_original([1,2,3])
calc_original([1,3,5,7])

#改造成可变参数
def calc(*numbers):#可变参数在函数调用时自动组装为一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2)
calc()

#如果传入的参数是list或者tuple
nums = [1,2,3]
calc(*nums)#*nums表示把nums这个list的所有元素作为可变参数穿进去


#关键字参数
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
def person(name,age,**kw):#关键字参数在函数内部自动组装为一个dict
    print('name:',name,'age:',age,'other:',kw)

print(person('Bob',35,city='Beijing'))
print(person('Adam',45,gender='M',job='Engineer'))

#简化字典参数
extra = {'city':'Beijing','job':'Engineer'}
print(person('Jack',24,**extra))#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

#检查关键字参数
def person_check(name,age,**kw):
    if 'city' in kw:
        pass #有city参数
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

print(person_check('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456))

#命名关键字参数
def person_limit(name,age,*,city,job):
    print(name,age,city,job)
print(person_limit('Jack',24,city='Beijing',job='Engineer'))

# print(person_limit('Jack',24,'Beijing','Engineer')) #必须传入参数名，否则报错

def person_limit_second(name,age,*args,city='BeiJing',job):#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
    print(name,age,args,city,job)

print(person_limit_second('denglong',30,1,2,3,4,city='shenzhen',job='Engineer'))





#参数组合
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def function_1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def function_2(a,b,c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(function_1(1,2))
print(function_1(1,2,c=3))
print(function_1(1,2,3,'a','b'))
print(function_1(1,2,3,'a','b',x=99))
print(function_2(1,2,d=99,ext=None))

#通过一个tuple和dict，也可以调用上述函数
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
function_1(*args,**kw)

args = (1,2,3)
kw = {'d':88,'x':'#'}
function_2(*args,**kw)

def product(x,*y):
    mul = 1 * x
    for n in y:
        mul = n * mul
    return mul

print(product(1))

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')