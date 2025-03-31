#从控制台输入要出的拳——石头1剪刀2布3，电脑随机出拳，比较胜负

#解题思路
#1 控制台输入，用到input函数，限制输入为整数
#2 对手是电脑，随机出拳，需用到random函数：import  random
#3 决定胜负
'''
你胜的情况：
你       电脑
剪刀     布
石头     剪刀
布       石头

平局的情况：
你和电脑出的一样

其他情况：
你输的情况
'''

import random
#自我尝试：三元表达式
user=int(input('输入你要出的拳，石头为1，剪刀为2，布为3：'))
computer=random.randint(1,3)    # 1,2,3 随机取数，在[1，3]范围内随机取整数
print('电脑出拳：石头') if (computer==1) else (print('电脑出拳：剪刀') if computer==2 else print('电脑出拳：布'))
print('你赢了') if ((user==1) and (computer==2)) or ((user==2) and (computer==3)) or ((user==3) and (computer==1)) else (print('平局') if user==computer  else print('你输了'))

#自我尝试：if语句
you=int(input('输入你要出的拳，石头为1，剪刀为2，布为3：'))
com=random.randint(1,3)
if com==1:
    print('电脑出拳：石头')
elif com==2:
    print('电脑出拳：剪刀')
else:
    print('电脑出拳：布')
if (you==1 and com==2) or (you==2 and com==3) or (you==3 and com==1):
    print('你赢了')
elif you==com:
    print('平手')
else:
    print('你输了')


#拓展：随机数
#电脑出拳
print(random.choice(['石头','剪刀','布']))
