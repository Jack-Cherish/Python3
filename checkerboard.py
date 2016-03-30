#Topic		:	要求输出国际象棋棋盘
#File Name	:	checkerboard.py
#Author		:	Jack Cui
#Created	:	30 March 2016
import sys
for i in range(8):
	for j in range(8):
		if (i + j) % 2 != 0:
			print(chr(219),end='')
			print(chr(219),end='')
		else:
			print('  ',end='')
	print('\n',end='')
