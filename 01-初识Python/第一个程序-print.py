#单独运行一个print语句时，前面不能有空格和tab键，否则报错
print('hello world')

# print语句
#print(*objects,sep=' ',end='/n') 默认用空格隔开，默认换行
print('的','我',4,56,8)

print('hello','world',sep=',')

print('hello','world',sep=',',end=' ')  # 不会自动换行，结尾用空格替代
print('哇哈哈')