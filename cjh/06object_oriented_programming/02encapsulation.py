# 封装 encapsulation
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线
# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用name、score这样的变量名
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 如果外部代码要获取name和score怎么办？可以给Student类增加get_name/set_score这样的方法
    # 为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


if __name__ == '__main__':
    zs = Student('zs', 99)
    zs.print_score()
    # print(zs.__name)  # AttributeError: 'Student' object has no attribute '__name'
    print(zs.get_name())  # zs

    # 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问name是因为Python解释器对外把name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
    # 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
    # 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉
    print(zs._Student__name)  # zs
