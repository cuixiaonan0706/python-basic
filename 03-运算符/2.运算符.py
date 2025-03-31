#计算优先级与数学运算一致：先乘除，后加减。幂是最高优先级，其次是乘除、取余取整，最后是加减。可以用（）调整优先级

print(10+20)    #加
print(20-10)    #减
print(10*10)    #乘
print(20/2)     #除
print(10//3)    #取整
print(10%3)     #取余
print(2**3)     #幂次

print('-'*50)

#多变量赋值
num1,num2,num3=1,2,'a'
print(num1)
print(num2)
print(num3)

print('-'*50)

a=100
a+=1        #等效于a=a+1,同理可得其他运算
print(a)

b=2
b/=2
print(b)