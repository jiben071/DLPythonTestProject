#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Hello, world")

print('The quick brown fox','jumps over','the lazy dog')

print(300)

print(100 + 200)

print('100 + 200 = ', 100 + 200)

# name = input("please enter your name:")
# print('hello',name)

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('''line1
line2
line3
''')

print(r'''hello,\n
world''')

age = 10
if age >= 10:
    print('adult')
else:
    print('teenager')


print(10 % 3)
print(10 // 3)

s1 = 72
s2 = 85
r = ((s2 - s1) / s1) * 100
print('提升了%.2f%%' % r)

#不可变元组
t = (1,)
t = ('a','b',['A','B'])
t[2][0] = 'X'
print(t)



age = 20
if age >= 18:
    print("Your age is ",age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello',x)

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
d.get('Michael')


s = set([1,2,3])
print(s)
s.add(4)
s.remove(4)

#交集 并集操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)

print(s1 | s2)

s3 = set((1,2,3))
# s3.add((1,[2,3]))
print(s3)

from DLFunctionTest import my_abs  #导入函数
print("你好 ",my_abs(-99))

exit()