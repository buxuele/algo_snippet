# author: fanchuangwater@gmail.com
# date: 2020/3/29 下午12:17
# 目的:

"""
在本地机器上执行结果是正确的。提交之后，超时 33 / 51 个通过测试用例。
目前等待官方解法。

    首先，看看最后需要的是什么样的结果。
    然后再分析怎样涉及自己的数据结构。
    返回从地铁站 startStation 到地铁站 endStation 的平均花费时间。

user1 = {start_time: 1, end_time: 2, start_pos： a, end_pos: b}
user2 = {start_time: 3, end_time: 4, start_pos： c, end_pos: d}
user3 = {start_time: 3, end_time: 4, start_pos： c, end_pos: d}

    ||
    ||
    ||  # 就变成这个熊样子了。这就类似json了。。。简直是刷新我对数据结构的认识了。
    \/

users = {
    user1_id:  {start_time: 1, end_time: 2, start_pos： a, end_pos: b},
    user2_id:  {start_time: 1, end_time: 2, start_pos： a, end_pos: b},
    user3_id:  {start_time: 1, end_time: 2, start_pos： a, end_pos: b},
    user4_id:  {start_time: 1, end_time: 2, start_pos： a, end_pos: b},
}

"""

class UndergroundSystem:
    def __init__(self):
        # 这里是不能给参数的 只能自己来涉及数据结构。
        # 可以自己来设计一种id
        self.users = {}
        self.trip = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # 记录当前的出发时间。
        if id not in self.users:
            self.users[str(id)] = {"start_pos": stationName, "start_time": t}
            # print(self.users)     # 这里可以显示出所有的出行记录。。。。
        else:
            # 如果这个用户再来的话，那就刷成新的数据。
            self.users[str(id)] = {"start_pos": stationName, "start_time": t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        trip_name = self.users[str(id)]["start_pos"] + stationName
        trip_cost = t - self.users[str(id)]["start_time"]
        if trip_name not in self.trip:
            self.trip[trip_name] = [trip_cost]     # 用一个元组来保存。
        else:
            self.trip[trip_name].append(trip_cost)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.trip[startStation+endStation]) / len(self.trip[startStation+endStation])


# ************** test start Now!!! ************
u = UndergroundSystem()
u.checkIn(45, "Leyton", 3)
u.checkIn(32, "Paradise", 8)
u.checkIn(27, "Leyton", 10)
u.checkOut(45, "Waterloo", 15)
u.checkOut(27, "Waterloo", 20)
u.checkOut(32, "Cambridge", 22)
x = u.getAverageTime("Paradise", "Cambridge")
print("x", x)

y = u.getAverageTime("Leyton", "Waterloo")
print("y", y)

u.checkIn(10, "Leyton", 24)
t = u.getAverageTime("Leyton", "Waterloo")
print("t", t)

u.checkOut(10, "Waterloo", 38)
z = u.getAverageTime("Leyton", "Waterloo")
print("z", z)

















# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

"""
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // 返回 14.0。从 "Paradise"（时刻 8）到 "Cambridge"(时刻 22)的行程只有一趟
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // 返回 11.0。总共有 2 躺从 "Leyton" 到 "Waterloo" 的行程，编号为 id=45 的乘客出发于 time=3 到达于 time=15，编号为 id=27 的乘客于 time=10 出发于 time=20 到达。所以平均时间为 ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // 返回 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // 返回 12.0

"""