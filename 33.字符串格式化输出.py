"""
字符串的格式化输出 是说在我们输出变量时，输出变量里面存的内容
1. 直接输出
2. 通过占位符输出
3. 通过f语法输出

"""

# 举例

name = 'lili'
age = 23
money = 66666.77854

# 直接输出   缺点是文字和变量之间要通过变量隔开

print("我的名字是:", name, '年龄是:', age, '工资是:', money)
# 我的名字是: lili 年龄是: 23 工资是: 66666.77854

# 通过占位符的方式，实现字符串的格式化输出
"""

%           占位符
%d          表示整数
%f          表示小数 
%s          表示字符串
%.2f        表示保留两位小数

"""
# 不用频繁的逗号，但是要多写后面一段内容
print('我的名字是:%s, 我的年龄是:%d, 我的工资是:%.2f' % (name, age, money))
# 我的名字是:lili, 我的年龄是:23, 我的工资是:66666.78


# 还可以通过在字符串前面加f的方式，f-format

# f-string就是允许在字符串中加表达式，并对{}中的表达式进行求值

print(f'我的名字是:{name}, 我的年龄是:{age}, 我的工资是:{money}')
# 我的名字是:lili, 我的年龄是:23, 我的工资是:66666.77854
