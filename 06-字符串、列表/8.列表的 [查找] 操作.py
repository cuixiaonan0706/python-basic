# 1）
# in 存在，在……里面True,否则为False
# not in 不在，True,否则为False
# list1=['cxn','cxn1','cxn2']
# name = input('需要查找的名字：')
# if name in list1:
#     print('找到了')
# else:
#     print('找不到')

# 2）
# count()  用来统计某个元素在列表中出现的次数
# listname.count(obj)   obj表示要统计的元素
# count 如返回0，则表示列表中不存在这个元素——可用count方法来判断某个元素是否存在
list2=['apple','banana','apple','par','banana','apple']
print(list2.count('apple'))
if list2.count('ipad'):     # count>0的情况，表示条件为True
    print('ipad在列表中')
else:                       # count次数为0，0代表False
    print('ipad不在列表中')

# 3）
# index   查找某个元素在列表中出现的位置
# 语法：listname.index(obj,start,end)
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums.index(3))
print(list2.index('apple'))     # 重复元素则返回第一个的位置