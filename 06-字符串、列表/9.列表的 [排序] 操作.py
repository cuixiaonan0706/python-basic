# reverse()   把原列表顺序倒置，逆置
li=[1,2,3,4,5]
print('原列表:',li)
li.reverse()            # 改变原列表
print('倒置列表:',li)

# sort() 排序
list=[1,5,3,6,8,4,9]
list.sort()       # 默认从小到大升序排序
print(list)
list.sort(reverse=True)     # 降序排序
print(list)

# 拓展
# sort只应用于list的方法
# sorted() 内建函数
list=[1,5,3,6,8,4,9]
a = sorted(list)        # 默认从小到大排序,不改变原列表
print(a)
print(list)


# 注意
print(list.sort())
''' 结果为None,
    因为sort()是对原表进行修改，就地排序，无返回值。
    如果与赋值、打印等方法一起使用，结果返回None. 
    虽然结果为None,但已改变原表 '''
print(sorted(list))
'''返回排序结果，因为sorted()对原表没有影响，产生新表。'''
print(sorted(list,reverse=True))
'''返回倒序列表可以使用上句代码'''