# 集合的定义：大括号包围元素，每个元素间用逗号隔开；
# 与字典的区别：字典键值对一一对应的关系，集合是没有的；
# 举例
# 定义：
# 1.直接{}
s1 = {10,20,30}
print(type(s1))     # <class 'set'>
print(s1)
# 2.用set()
s2=set('abcdefg')
print(type(s2))
print(s2)       # {'c', 'g', 'd', 'f', 'e', 'a', 'b'}顺序随机

# 定义一个空集合
s3={}               # 系统认为这是定义一个空字典
print(type(s3))     # <class 'dict'>
s4=set()            # 定义一个空集合
print(type(s4))     # <class 'set'>
print(s4)

# 集合的特性：无序不重复，不支持下标操作


# 集合的常见操作

# 一、增
s1={10,20}
# 1.add  添加具体的某元素
s1.add(1)       # 添加‘1’元素
print(s1)
s1.add(10)      # 添加重复元素是无效操作
print(s1)       # {1, 10, 20}

# 2.update() 追加的数据必须是可迭代对象（如列表、集合、字典、元组）
s1={10,20}
s1.update(['a'])        # 添加列表
print(s1)
s1.update((888,999))    # 添加元组，元组不能只添加一个
print(s1)
s1.update({'id':'1'})   # 添加字典，只添加了key(字典的键值对是一个整体，代表一个元素)
print(s1)               # {999, 'a', 10, 20, 888, 'name'}

'''把xy合并，并且去重'''
x={'apple','banana','cherry'}
y={'google','apple','baidu'}
x.update(y)
print(x)
# 注意此时不能使用add，add方法添加具体的元素

# 二、删除
# 1.remove()    删除集合中指定的数据，如果数据不存在则报错
s1={10,20}
s1.remove(10)
print(s1)
# s1.remove(10)   # 没有则报错

# 2.discard() 丢弃    删除集合中指定的数据，，如果数据不存在则报错
s1={10,20}
s1.discard(10)
print(s1)
s1.discard(10)
# print(s1)   # 没有则报错

# 3.pop() 随即删除集合中的某个数据
s1={1,2,3,4,5,6,7,8,9,10}
print(s1.pop())     # 返回删除的数，前两个函数返回的是none

# 三
# 1.交集 &
a = {1,2,3,4}
b = {2,3,4,5}
se = a&b
print(se)

# 2.并集 |
se = a|b
print(se)

