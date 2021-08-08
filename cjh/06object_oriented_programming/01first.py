# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
# 面向对象的设计思想是抽象出Class(Student)，根据Class创建Instance(zs)
# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与init方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去

# >>>>>>数据封装<<<<<<<
# 面向对象编程的一个重要特点就是数据封装。在Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据
# 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法, 例如：print_score
# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入

# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同

class Student(object):  # object代表该类是从哪个类继承下来的
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
    # 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
    def print_score(self):
        print('%s: %s' % (self.name, self.score))


if __name__ == '__main__':
    zs = Student("zs", 99)
    ls = Student("ls", 80)
    zs.print_score()  # zs: 99
    zs.age = 18
    print(zs.age)  # 18
    print(ls.age)  # AttributeError: 'Student' object has no attribute 'age'
