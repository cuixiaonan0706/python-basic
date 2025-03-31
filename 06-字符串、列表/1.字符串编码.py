# 字符编码：本质是二进制数据与语言文字的一一对应关系
# 字符——（翻译）——二进制
# unicode  兼容万国语言
# utf-8  对不同的字符用不同的长度来表示，编码的中文使用了3个字节
# gbk 用来专门解决中文编码的，双字节
# 中文程序开发：使用gbk

# encode编码：将字符转换成字节流（二进制数据流）
a = 'hello'
print(type(a))      # <class 'str'>
b = b'world'        # b'world'
print(b)            # <class 'bytes'> 字节码，即字节流
print(type(b))

a = 'sister'
print(a)
a1 = a.encode()     # 给a进行编码，把字符串转换成二进制数据流
print(a1)           # b'sister'

# decode解码：解码的本质，将字节流解析为字符（还原字符串）
a2 = a1.decode()
print(a2)           # sister
print(type(a2))     # <class 'str'>