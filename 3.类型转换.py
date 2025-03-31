#数值类型：int float bool complex
#数据结构类型：str list dict tuple
#想要转换成什么类型，就用哪个函数

a=1
print(str(a))
print(type(str(a)))     #把a转换成字符串类型

b='2'
b1=int(b)
print(type(b1))     #若本身不是整型，则会转换失败。如‘a’无法转换成整型
