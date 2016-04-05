#Topic 	        :       编程找出1000以内的所有完全数
#File Name      :       PerfectNumber.py
#Author         :       Jack Cui
#Created        :    	5 April  2016
for num in range(2,1001):
	result = []
	flag = num	#打印标志位
	for factor in range(1,num):
		if num % factor == 0:
			flag -= factor 
			result.append(factor)
	if flag == 0:
		print(num,end='=')
		result_length = len(result)	
		for i in range(result_length):
			if i != result_length - 1:
				print(result[i],end='+')
			else:
				print(result[i])
