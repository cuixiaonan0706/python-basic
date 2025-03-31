# 一、字符串——查
# 1.find ：字符串序列.find(str，开始下标，结束下标)
# 检测子串str是否包含在原字符串myst中，如果在则返回第一次找到的索引值，否则返回-1

a = 'hello world'
print(a.find('h'))         # 返回第一次找到时的索引值（开始索引值）
print(a.find('hello'))
print(a.find('l',1,5))  # 在1~5的范围去查找
print(a.find('h',1,4))  #找不到返回-1

# 2.index查找索引 ：字符串序列.index(str，开始下标，结束下标)
# 与find方法一样，只不过如果str不在mystr中会报一个异常
print(a.index('h',0,4))
# print(a.index('h',1,4))     # 找不到会报错

# 3.count：字符串序列.count(str，开始下标，结束下标)  查找子串在原字符串中出现的次数
print(a.count('l'))
print(a.count('h',0,4))
print(a.count('h',1,4))


# 二、修改
# 1.replace：字符串序列.replace(旧子串，新子串，替换次数)
mystr = 'hello world'
print(mystr.replace('l','8'))           # he88o wor8d
print(mystr.replace('l','8',2))  # he88o world

# 2.split 分割：字符串序列.split(str，切的次数)  用str来切原字符串
b = 'he,ool,wor,ld'
print(b.split(','))
print(b.split(',',2))
print(mystr.split(' '))

# 3.capitalize  第一个字母变成大写
print(a.capitalize())

# 4.lower   把字符串所有大写转化成小写
c='HELLO'
print(c.lower())

# 5.upper   把字符串所有小写转化成大写
print(a.upper())

# 6.title 把字符串的每个单词首字母大写
print(a.title())


# 三、判断
# 1.islower()  检测字符串是否都由小写字母组成（True False）
print(a.islower())

# 2.isupper()  检测字符串是否都由大写字母组成（True False）
print(mystr.isupper())

# 3.isdigit()  是否是数字
j = 0
mystr1='hello123'
for i in mystr1:
    if i.isdigit():     # i.isdigit()返回值为True或False，表示判断字符串的每个字符是否为数字。为真时，表示为数字，执行if里面的语句
        j += 1          # 统计是数字的个数
print(j)                # mystr1中数字的个数

# 4.startwith()  判断字符串是否以什么开头
print(a.startswith('h'))

# 5.endswith()  判断字符串是否以什么结尾
print(a.endswith('h'))


# 四、增
# 1.+
name='a'
name2='b'
info=name+name2
print(info)

# 2.join
print('*'.join(a))      # h*e*l*l*o* *w*o*r*l*d

# 五、删
# 1.lstrip()  删除字符串左边的空白字符
a1='  hello world'
print(a1)
print(a1.lstrip())

# 2.rstrip()  删除字符串右边的空白字符
# 3.strip()  删除字符串两边的空白字符