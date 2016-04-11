#Topic 	        :       打印出菱图案
#File Name      :       Diamond.py
#Author         :       Jack Cui
#Created        :    	11 April 2016
for i in range(4):
	for line in range(3-i):
		print(' ',sep='',end='')
	for column in range(2*i+1):
		print('*',sep='',end='')
	print('')
for i in range(3):
	for line in range(i+1):
		print(' ',sep='',end='')
	for column in range(5-2*i):
		print('*',sep='',end='')
	print('')
