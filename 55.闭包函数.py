"""
def f():
    a = 5
    def g():
        print(a = 5)
        ........
闭包现象：
即是说，函数嵌套的时候，内层函数用到了外层函数中的变量，导致函数执行结束时，该变量没有被释放，而是被记录了下来
这里g是闭包函数
"""


# 函数里面嵌套了另外一个函数，外部的函数叫做外函数，内部的函数叫做内函数
# 如果在一个外部函数中定义了一个内部函数，并且外部函数的返回值是内部函数，就构成了一个闭包，则这个内置函数就被称为闭包


# 举一个例子

def outer(x):
    def inner(y):
        return x + y
    return inner


add = outer(5)

print(add(3))  # 8



























