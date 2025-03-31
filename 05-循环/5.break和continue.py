# break 和 continue 只能够在循环内使用

# break: 退出所在循环的当前循环，不再当层循环（即不再继续当层循环）
#1） while循环
a = 0
while a<3:
    a += 1
    print(a)
    break       #不再循环

while a < 5:
    a = a + 1
    if a == 3:
        break
    print(a)
else:
    print('已经打印完成了')    #不执行
# 循环可以else配对使用，else下方缩进的代码是：当循环正常结束之后会执行

#2） for循环
for i in range(3):
    print(i)    # 0
    break

for i in range(5):
    if i == 3:
        break
    print(i)

# break只对当前所在循环有效
# 循环嵌套中的break
for i in range(5):
    print('——外循环代码——')
    for i in range(3):      # break跳出的是range(3)条件的循环
        if i == 3:
            break
        else:
            print('内循环语句')


# continue: 结束循环，结束的是当前循环的本轮循环(continue后面的代码不再执行)，继续下一轮循环
#1） while循环
a = 0
while a < 5:
    a = a + 1   # 如果放在最后一行，则会出现死循环，因为continue后面的代码不执行，a就不会自加
    if a == 3:
        continue
    print(a)

#2） for循环
for i in range(5):
    if i == 3:
        continue
    print(i)