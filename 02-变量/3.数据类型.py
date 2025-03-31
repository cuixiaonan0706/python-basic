# 字符串 str
str1='hello'
print(str1)
print(type(str1))

#三引号    用在变量定义里，用来定义多行字符串的内容
#注释： 三对单引号/双引号 用来进行多行注释
hi='''
hi
hello
python
'''
print(hi)

# 字符串内部使用双引号或单引号
print('hello \'w\'orld')    # \为转义字符


#字符串的运算
#1 字符串的拼接 +
a= 'hello'
b= 'world'
print(a+b)
print(a+' '+b)

#2 复制：重复输出字符串 *
print(a*2)

#3 in / not in 在 / 不在 里面
print('h' in a)         #TRUE 表示字符串h在a里面
print('w' not in a)

#4 r\R 原样输出后面的内容
print('hello \n hello')
print(r'\n')    #r后面单引号内的内容将原样输出
print(r'hello \n hello')

