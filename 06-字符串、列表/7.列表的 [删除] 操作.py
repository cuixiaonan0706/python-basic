# 1) del:   del listname    删除整个列表
s = list('hello')       # 把字符串转化成列表
print(s)
# del s
# print(s)

# del listname[index]   通过索引访问值
s = [1,2,3,4]
del s[1]
print(s)

# del 删除多个值
del s[2:5]
print(s)


# 2）pop()
# listname.pop(index)   index默认不写，默认会删除列表中最后一个元素
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums)
nums.pop(3)
print(nums)
nums.pop()
print(nums)

# 3） remove() 删除指定元素，无则报错；如果有相同元素，删除第一个
nums=[1,2,3,4,5,111,5,6,7]
nums.remove(2)
print(nums)
nums.remove(5)      # 只会删除第一个符合的值
print(nums)

a=['a','a','p','p','l','e']
a.remove('a')
print(a)

# 4）clear() 删除列表所有元素
a.clear()
print(a)

# 小结：
# 根据位置索引删除，用del 或 pop
# 根据值进行删除，用remove
# 删除整个列表元素，用clear