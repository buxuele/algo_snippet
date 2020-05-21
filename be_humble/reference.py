# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午11:02
# 目的: 本质上，python内部的调用，实际调用是对象的引用(reference),即变量名。


#　1.　
x = "some"
y = x
print(x is y)
# 这里的删除，只是删除了ｘ这个作为对象的引用，删除的是引用，
# 而内存中的实际对象“some”是不收影响的。
del x
print(y)    # some
print()

# 2.
name = "test"


def add_chars(a):
    # 传入的变量名和全局变量名指向的是同一个对象，所以他们的地址是一样的。
    print(id(a))
    print(id(name))

    b = a
    # 但是这里就创建了一个新的对象，并且对象的指向还是ａ,
    # 变量名还是a
    a += "hi"
    print(a, id(a))
    print(b, id(b))


add_chars(name)
print()
print(name)


