
# coding=UTF-8

myName = raw_input("您的名字?")
age = int(raw_input("您的年龄?"))
differential = int(raw_input("你对象比你大几岁?"))
GFage = age+differential
forever = "永远"

print """



		经过计算后,您的个人信息如下:



"""
# print "hello world","如果不声明编码,则不支持中文"	#甚至注释都不行哦~
print "%s%s%i岁" % (myName,forever,age)
print "%s对象比%s大%i岁,今年%d岁" % (myName,myName,differential,GFage)


