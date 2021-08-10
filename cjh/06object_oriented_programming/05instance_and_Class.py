# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    age = 18

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    s = Student("jack")
    s.score = 90
    print(s.name, s.score)  # jack 90

    # 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
    # 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。
    print(s.age)  # 实例属性 18
    print(Student.age)  # 类属性 18
    # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的age属性
    s.age = 19
    print(s.age)  # 19
    print(Student.age)  # 18
    # 如果删除实例的age属性, 再次调用s.age，由于实例的age属性没有找到，类的age属性就显示出来了
    del s.age
    print(s.age)  # 18
    # 从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
