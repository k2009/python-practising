# coding=UTF8


#切片


list = [1,2,3,4,5,6,7,8,9,0]

print list
print list[0]		# 感觉类似数组操作,其实前面这俩都和js里一样
print list[:]		# [开始:结束] 从开始处开始,结束处结束 PS:并不包括结束
print list[-1]		# [-1] 戴表最后一个
print list[2::2]	# [开始::Number]从开始处开始,表示每隔Number个获取一个
print list[::-1]	# 翻转操作
