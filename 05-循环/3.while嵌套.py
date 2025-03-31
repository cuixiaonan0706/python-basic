'''
while 条件：   #外循环
    while 条件：   #内循环
        print('我错了')
    print('罚！')
'''

j = 0
while j <3:     #连续三天执行的动作
    i = 0
    while i < 3:    # 每天要说三遍‘我真厉害’
        print('我真厉害！')
        i += 1
    print('出门！')
    print('一天过去了……')
    j += 1
print('3天都过去了')


# 使用while嵌套打印图形
'''前置知识：print('*' * 5) 字符串的复制
思路: 把5变成变量i，i代表行数 ;  i<=i<=5 '''
i = 1
while i <= 5:
    print('* ' * i)
    i += 1

'''方法2：利用循环嵌套打印'''
# *             1个星，4个空
# * *           2个星，3个空
# * * *         第三行，最多3列
# * * * *       col列方向执行最多四次
# * * * * *

# 1）进行5次循环，每次循环代表一行，定义一个变量row来代表行数；
# 2）从上图可以看出，每一行实际上是5个位置
# 3）定义一个列数col ; col <= row

row = 1
while row <= 5:
    col = 1     # 定义列的初始值
    while col <= row:
        print('*',end=' ')
        col += 1
    print()     # 默认换行，手动换行
    row += 1


# 练习：打印九九乘法表，使用while嵌套
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}',end='\t')
        #法2：print('%d * %d = %d' %(i,j,i*j),end='\t')
        #法3：print('{}*{}={}'.format(i,j,i*j),end='\t')
        i += 1
    print()
    j += 1