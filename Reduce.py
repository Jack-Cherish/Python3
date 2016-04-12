#Topic 	        :       求2/1、3/2、5/3、8/5、13/8、21/13...
#			求出这个数列的前20项之和
#File Name      :       Map-Reduce.py
#Author         :       Jack Cui
#Created        :    	13 April 2016
from functools import reduce
a = 2
b = 1
Arr = []
num = int(input("请输入要计算的项数："))
for i in range(num):
	Arr.append(a / b)
	a , b = b , a + b
print(reduce(lambda x,y:x+y,Arr))
