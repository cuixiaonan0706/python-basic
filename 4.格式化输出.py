#格式化输出：按照我们自己想要输出的格式，先定义一个模板，照着模板输出
#格式化输出思路：首先定义模板，然后照着模板把变量填进去
#格式化输出 print(模板 % 变量名)

# 1)
# %s 字符串形式输出
age=18
name='Wilia'
print('我的名字是%s,年龄是%d' % (name,age)) #绿色引用的部分是模板，%后填写对应变量名

# %f 浮点数
a=1.3333
print('%f' % a)    #默认保留6位小数
print('%.2f' % a)  #保留两位小数

# 十进制: %d
num1 = 10.45
print('数字是： %d' % num1 )

#八进制：满8进1 %o
num2 = 9
print('数字是：%o' % num2)


#2）
# format() 函数
#1 不带编号。即{}
print('{},{}'.format(1,2))
a='hello'
b='world'
print('{} {}'.format(a,b))

#2 带数字编号，课调换顺序，即{1} {2}
print('{0} {1}'.format('hello','world'))
print('{0} {1} {0}'.format('hello','world'))    #第一个元素对应的编号是0，第二个对应的是1，……

#3 设置参数
print('用户名：{name},地址:{url}'.format(name='wilia',url='www.abcdefg.com'))


#3）f'{表达式}’ 格式输出,也不需要考虑数据
print(f'名字是：{"cxn"},年龄是：{20}')
print(f'名字是：{'cxn'},年龄是：{20}岁')     #内部引号单双都可以
a='cc';b=23
print(f'名字是：{a},年龄是：{b}')

#疑问点：后两种输出形式如何定义输出类型呢？如length=12.5，输出时想只保留整数
length=12.5
print(f'长度是：{length}')

