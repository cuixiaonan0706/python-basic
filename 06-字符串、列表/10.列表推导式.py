list = [1,2,3,4,5,6,7,8,9]
print([i*2 for i in list])  # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# for循环
list1=[1,2,3,4,5]
list2=[]
for i in list1:
    list2.append(i*2)
print(list2)

# while循环（以下代码成立的条件是原列表是1：10：1）
li1=[1,2,3,4,5,6,7,8,9]
li2=[]
i = 0
while i < len(li1)+1:
    if i in li1:
        li2.append(i*2)
    i += 1
print(li2)