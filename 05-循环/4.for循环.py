'''for 临时变量 in 可迭代对象：
'''
# 可迭代对象：能通过for循环一个个的把数取出来的对象
# range()函数
# range(start,end,step)   range(1,5,2)范围是左闭右开,[1,5)
# start 计数开始的位置，默认是0开始。如range(5)代表[0，5)
# end 计数结束的位置
# step 每次跳跃的间距，不填默认为1
for i in range(5):
    print(i)

# 计算1-100累计和
sum = 0
for i in range(1,101):
    sum = i + sum
print(sum)

#打印九九乘法表
for j in range(1,10):
    for i in range(1,j+1):  # i的范围是j+1,即i<=j
        print(f'{i}*{j}={i*j}',end='\t')
    print()