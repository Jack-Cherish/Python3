#Topic          :       汉诺塔   
#File Name      :       Hanoi.py
#Author         :       Jack Cui
#Created        :       7 April 2016

#第一个塔A为初始塔，中间的塔B为中转塔，最后一个塔C为目标塔
def move(n,n_from,n_to):
	global i	#声明i是全局变量
	print('第%d步：%d号盘子  初始塔%s-->目标塔%s' % (i,n,n_from,n_to)) 
	i += 1
#汉诺塔移动函数，将n个盘子（借助中转塔）由初始塔上移动到目标塔上
def hanoi(n,n_from,n_transit,n_to):
	if n == 1:
		move(1,n_from,n_to)	#只有一个盘子直接将初始塔上A的盘子移动到目标塔C
	else:
		hanoi(n-1,n_from,n_to,n_transit)#先将初始塔A的前n-1个盘子借助目标塔C移动到中转塔B上
		move(n,n_from,n_to)		#将初始塔A上最后一个盘子移动到目标塔C上
		hanoi(n-1,n_transit,n_from,n_to)#最后将中转塔上的n-1个盘子移动到目标塔上

if __name__ == '__main__':
	i = 1
	n = int(input('请输入盘子的个数：'))
	print('盘子移动的方法如下：')
	hanoi(n,'A','B','C')
