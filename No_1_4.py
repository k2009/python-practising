# coding=UTF8
#新式类
def test_1():
	# super继承
	# class FooParent(object):  
	#     def __init__(self):  
	#         self.parent = 'I\'m the parent.'  
	#         print 'Parent'  
	      
	#     def bar(self,message):  
	#         print message,'from Parent'  
	  
	# class FooChild(FooParent):  
	#     def __init__(self):  
	#         super(FooChild,self).__init__()  
	#         print 'Child'  
	          
	#     def bar(self,message):  
	#         super(FooChild, self).bar(message)  
	#         print 'Child bar fuction'  
	#         print self.parent  
	 


	# 普通继承

	class FooParent(object):  
	    def __init__(self):  
	        self.parent = 'I\'m the parent.'  
	        print 'Parent'  
	      
	    def bar(self,message):  
	        print message, 'from Parent'  
	          
	class FooChild(FooParent):  
	    def __init__(self):  
	        FooParent.__init__(self)  
	        print 'Child'  
	          
	    def bar(self,message):  
	        FooParent.bar(self,message)  
	        print 'Child bar function.'  
	        print self.parent  
	          
	# 从运行结果上看，普通继承和super继承是一样的。但是其实它们的内部运行机制不一样，这一点在多重继承时体现得很明显。在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）。
	# 注意super继承只能用于新式类，用于经典类时就会报错。
	# 新式类：必须有继承的类，如果没什么想继承的，那就继承object	广度优先的查找原则
	# 经典类：没有父类，如果此时调用super就会出现错误：『super() argument 1 must be type, not classobj』	从左至右，深度优先的查找原则 
	fooChild = FooChild()  
	fooChild.bar('HelloWorld')  



# test_1()




# 经典类
def test_2():
	class P1():
	    def foo(self):
	        print 'p1-foo'

	class P2():
	    def foo(self):
	        print 'p2-foo'
	    def bar(self):
	        print 'p2-bar'

	class C1(P1,P2):
	    pass

	class C2(P1,P2):
	    def bar(self):
	        print 'C2-bar'

	class D(C1,C2):
		# def foo(self):	#如果D自身有就先调用D自身的function,没有就向上查找
		# 	print 'D-foo'
		pass

	d=D()
	d.foo()
	d.bar()

test_2()








