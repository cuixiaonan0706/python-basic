# 元组 <tuple>
# 元组的特性：不能够被修改、不支持删除（与列表的最大不同）
# 元组的定义：元素由小括号包围，每个元素之间用逗号隔开，如（1，2，3）
# 意义：因为元素不可修改和删除，所以提高了代码编写的安全性。能用元组尽量用元组。

# 一、元组的特性
nums=(10,20,30)
print(type(nums))
print(nums[0])

''' 
    nums[0]=100     # 尝试修改，报错
    print(nums)     # TypeError: 'tuple' object does not support item assignment

    del nums[0]     # 尝试删除，报错
    print(nums)     # TypeError: 'tuple' object doesn't support item deletion
'''

# 元组的定义
# 多个数据的元组
t1=(1,2,3)
print(t1)
# 定义单个数据的元组，必须要加一个逗号
t2=(10)             # 与 t2 = 10 同效
t3=(10,)
print(t2)
print(t3)
print(type(t2))     # <class 'int'>
print(type(t3))     # <class 'tuple'>
