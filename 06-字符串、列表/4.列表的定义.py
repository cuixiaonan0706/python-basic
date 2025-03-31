# 列表：一次性存储多个数据
li = ['a','b','c']  # 列表的定义：中括号包围所有的元素，每个元素间用逗号隔开
# 特性：有序；存储多个数据；元素可以是不同类型
list1 = [1,1.5,'a']
print(list1)

print(li[0])
print(li[2])
print(li[-1])

print('——'*5)

# 循环读取 for
for i in li:
    print(i)

print('——'*5)

# while
li_len=len(li)  # len 求列表的元素个数
i = 0
while i < li_len:
    print(li[i])
    i += 1
