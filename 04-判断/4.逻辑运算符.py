# and 与
# x and y : 同真为真，一假全假
# 参数从左向右解析的，一旦结果可以确定就停止
#1） 当x为真时，要看y. 当y为真时，返回值为真。y为假则返回值为假。此时，整个表达式的值即为y的值
#2） 当x为假时，整个表达式的返回值为假。

# or 或
# 1）当x为真，返回真
# 2）当x为假时，y为真则返回真，反之返回假。即此时返回值取决于y

x=1
y= False
print(x and y)
print(x or y)

a=1
b=2
print(a and b)  # 3 :表示x为真
print(x or y)

# not 非
print(not 0)
print(not 1)


#练习
age=int(input('请输入你的年龄：'))
if age>=0 and age <=120:
    print('输入正确')
else:
    print('请重新输入')

python_score=int(input('输入你的python成绩：'))
c_score=int(input('输入你的c语言成绩：'))
if python_score>60 or c_score>60:
    print('合格')
else:
    print('不合格')

employer=input('输入t或f表示你是否就职于xx公司：')
if employer=='t':   #可以直接写 if employer:
    is_employer=True
    print('通过')
elif employer=='f':
    is_employer=False
    print('不是本公司员工，禁止入内')
else:
    print('错误，请重试！')