from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
    # value属性则是自动赋给成员的int常量，默认从1开始计数

    # 访问这些枚举类型可以有若干种方法
    print(Weekday.Sun)  # Weekday.Sun
    print(Weekday['Sun'])  # Weekday.Sun
    print(Weekday(1))  # Weekday.Sun
    print(Weekday.Thu.value)  # 4
    print(Weekday.Mon == Weekday.Mon)  # True
    # Weekday(7)  # ValueError: 7 is not a valid Weekday
    # 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
