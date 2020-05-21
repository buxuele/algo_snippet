# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午10:29
# 目的: 　这个例子能很好地解释　静态方法　和　类方法。


class CoffeeShop:
    specialty = 'espresso'

    def __init__(self, price):
        self.coffee_price = price
        self.taste = "sweet"

    def make_coffee(self):
        print(f'making {self.specialty} for ${self.coffee_price}')

    # 不能更改类或实例，一般作为工具方法
    @staticmethod
    def check_weather():
        print("A good day!")

    @classmethod
    def change_specialty(cls, specialty):
        cls.specialty = specialty
        print(f'Specialty changed to {specialty}')


coffee = CoffeeShop(2)
coffee.make_coffee()
coffee.change_specialty("nice")
coffee.make_coffee()

"""
输出：
making espresso for $2
Specialty changed to nice
making nice for $2            ＃　！！！！
"""





