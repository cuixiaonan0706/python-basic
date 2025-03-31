#比较运算符
a=1;b=2
print(a==b)
print(a<b)
print(a<=b)


#else一般用在最后，即所有条件都不满足时使用
#elif else 必须和if联系使用，不能单独使用

age=19
if age<16:
    print('回家吧')
elif age>=16 and age<=18:   #16<=age<=18
    print('即将成年，玩吧，玩了你就废了')
else:
    print('欢迎光临')

a=0
if a<0:
    print(0)
elif a==0:
    print(1)
else:
    print(2)

#成绩示例
score=int(input('请输入你的成绩：'))
if score >= 90 and score <= 100:
    print('特优')
elif score >= 80 and score <= 90:
    print('优秀')
elif score >= 70 and score <= 80:
    print('良好')
elif score >= 0 and score <= 70:
    print('请继续努力')
else:
    print('无效成绩')