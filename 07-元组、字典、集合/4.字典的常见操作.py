# 常见操作一
# 1.修改
dict1={'name':'Tom','age':20,'gender':'女'}
dict1['name']='Amy'
print(dict1)

# 2.添加
dict1['id']=110
print(dict1)

# 小结：对于key，无则添加，有则覆盖（值覆盖）

# 3.删除
# del
del dict1['id']
print(dict1)
# clear()
dict1.clear()
print(dict1)

# 4.查找
dict1={'name':'Tom','age':20,'gender':'女'}
print(dict1['name'])        # 通过key值查找
print(len(dict1))           # 查看键值对的数量

# 常见操作二
# keys() 查看所有键，返回列表
print(dict1.keys())
# values() 查看所有的值，返回列表
print(dict1.values())
# items() 可理解为‘项’，查看所有键、值，返回列表
print(dict1.items())

# 字典的循环遍历
# 1.for …… in
# 循环遍历value
dict1={'name':['Tom','Amy'],'age':[20,19],'id':['01','02']}
for value in dict1.values():    # 此句代码中的value为自定义变量
    print(value)                # 返回字典中value的类型
# 循环遍历key
for key in dict1.keys():        # 此句代码中的key为自定义变量
    print(key)
# 循环遍历items()
for item in dict1.items():      # 此句代码中的item为自定义变量
    print(item)                 # 返回为元组
# 循环输出 key=value
for key,value in dict1.items():
    print(f'{key}={value}')