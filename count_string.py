#Topic		:	输入一行字符，分别统计出其中英文字母,
#			空格和其他字符的个数
#File Name	:	count_string.py
#Author		:	Jack Cui
#Created 	:	1 April 2016
str = input('please input a string:\n')
letter = 0
space = 0
digit = 0
other = 0
for i in str:
	if i.isalpha():
		letter += 1
	elif i.isspace():
		space += 1
	elif i.isdigit():
		digit += 1
	else:
		other += 1
print('letter = %d,space = %d,digit = %d,other = %d' % (letter,space,digit,other))
