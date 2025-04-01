# 一、基础操作
# 一）+  拼接
# 1）字符串
str1='aa'
str2='bb'
str3=str1+str2
print(str3)
# 2）列表
list1= [1,2]
list2=[3,4]
list3=list1+list2
print(list3)
# 3）元组
t1=(1,2)
t2=(3,4)
t3=t1+t2
print(t3)
# 二）*  复制
# 1.列表
list1=['a']
print(list1*5)
# 2.字符串
str1='a'
print(str1*5)
# 三）in 存在 ；not in 不存在
# 1.列表
list1=['a','b','c']
print('a' in list1)     # 结果为True 或 False


#二、公共操作
# 1. len() 字符串 列表 元组 集合 字典，都适用
s1={10,20,30}
print(len(s1))

# 2. del 删除
str1='abc'
del str1

# 3. max() 最大值
# 列表
list1=[1,2,3,4,6]
print(max(list1))

# 4. min() 最小值
print(min(list1))

# 5. range()
for i in range(5):
    print(i)

# 6.enumerate()     效果是（下标，数据） 一一列出，通常用for来遍历
list1=['a','b','c']
for i in enumerate(list1):
    print(i)
''' 运行结果：
    (0, 'a')
    (1, 'b')
    (2, 'c')'''