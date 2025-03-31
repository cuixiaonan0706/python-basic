# 一、增
# 1）+
language=['python','C++','Java']
birthday=[1991,1998,1995]
info=language+birthday
print(info)

# 2）insert()插入元素
# 语法： listname.insert(index,obj)
l=['python','R','C++','Java']
l.insert(1,'C')     # 在1的位置插入’C‘
print(l)    # 改变的是原列表
t=('c#','go')
l.insert(2,t)   # 把元组当成一个整体插入
print(l)

# 3）append() 末尾添加元素
# 语法：listname.append(obj)
l.append('SAS')
print(l)
a=('spss','mysql')
l.append(a)
print(l)

# 4）extend()
# 语法：listname.extend()在列表末尾添加obj，并且把obj中的元素拆分成单个
b=('matlab','rstudio')
l.extend(b)
print(l)