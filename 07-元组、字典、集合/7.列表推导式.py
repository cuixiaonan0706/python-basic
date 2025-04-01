''' 设定一个空列表，
    利用while循环，
    在这个列表中填充数字1~9'''
#1. while
list1 = []
i = 0
while i <= 9:
    list1.append(i)
    i+=1
print(list1)

#2. for
list2=[]
i = 0
for i in range(10):
    list2.append(i)
print(list2)

# 3. 推导式
# 列表推导式
list1=[i for i in range(10)]
print(list1)
# 元组推导式
t1=(i for i in range(10))
print(t1)           # 返回地址
print(tuple(t1))    # 返回元组
# 字典推导式
dict1={i:i**2 for i in range(1,10)}     # x:x^2
print(dict1)
# 集合推导式
set1={i for i in range(10)}
print(set1)
print(type(set1))
'''利用集合推导式，对列表/元组进行去重'''
list1=[1,1,2,2,3,3,4,4]
t1=(1,1,2,2,3,3,4,4)
set1={i for i in list1}
set2={i for i in t1}
print(set1)
print(set2)