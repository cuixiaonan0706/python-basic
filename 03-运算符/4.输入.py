#input()输入函数;print()输出函数
#输入特点：
#1 当程序执行到input，等待用户输入，输入完成后才会继续向下执行
#2 input接收用户输入后，一般存储到变量，方便使用
#3 input会把接收到的任意用户输入的数据都当作字符串处理

data=input('请输入：')
print(data)
print(type(data))

weight=float(input('请输入物体质量（KG）：'))
print(weight)
print(type(weight))

x=eval(input('请输入一个数:'))    #eval()会自动对内容进行转化成数字
print(x)