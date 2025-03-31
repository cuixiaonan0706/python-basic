#if True:
#   print('条件成立执行的代码1')
#   print('条件成立执行的代码2')
#
#print('我是无论条件是否成立都会执行的代码')

#True和False的界定
# 1.任何非零和非空对象都为真，解释为True
# 2.数字0、空对象、None对象均为假，解释为False
# 3.判断的返回值为True或False

a=True          #True默认逻辑值为1，False默认逻辑值为0
b=1
print(a+b)      #2

print(not 0)    #非零时

#判断年龄是否满18
age=eval(input('输入你的年龄：'))
if age>=18:
    print('yes')
else:
    print('回家吧 回家吧孩子 好不好？')
