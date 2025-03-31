# 变量的命名
# 标识符的规范
# 关键字：Python内部已经使用的标识符
#怎么查看？
import keyword
from keyword import kwlist
print(keyword,kwlist)

#标识符规定
#1 只能由数字、字母、下划线组成
#2 不能以数字开头
#3 不能是关键字
#4 区分大小写

# 变量名的命名规则
#1 大驼峰：每个单词首字母大写， 如 MyName
#2 小驼峰：从第二个字母开始，单词首字母大写，如 myName
#3 下划线：my_name
