# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午10:15
# 目的: What is a decorator?
# https://towardsdatascience.com/53-python-interview-questions-and-answers-91fa311eec3f


def logging(func):
    def log_function_called():
        print(f'{func} is called!')
        func()
    return log_function_called


def my_name():
    print("funchuang")


@logging
def friends_name():
    print("someone X")


my_name()
friends_name()

