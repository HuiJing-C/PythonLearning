# 把变量从内存中变成可存储或传输的过程称之为序列化, 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思

import pickle
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


if __name__ == '__main__':
    # pickle.dumps()方法把任意对象序列化成一个bytes
    # pickle.dump()直接把对象序列化后写入一个file-like Object
    d = {'A': 1, "B": 2}
    print(
        pickle.dumps(d))  # b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01A\x94K\x01\x8c\x01B\x94K\x02u.'
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()
    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
    f2 = open('dump.txt', 'rb')
    w = pickle.load(f2)
    f2.close()
    print(w)  # {'A': 1, 'B': 2}  这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已

    # >>>>>>>>>>>>>>JSON<<<<<<<<<<<<<<<<
    dd = dict(name='cjh', age=18, score=99.9, male=True)
    print(json.dumps(dd))  # {"name": "cjh", "age": 18, "score": 99.9, "male": true}
    # dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object

    # 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
    print(json.loads(
        '{"name": "cjh", "age": 18, "score": 99.9, "male": true}'))  # {'name': 'cjh', 'age': 18, 'score': 99.9, 'male': True}

    # JSON进阶
    # Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
    s = Student('cjh', 20, 88)
    # print(json.dumps(s))  # TypeError: Object of type Student is not JSON serializable
    # 错误的原因是Student对象不是一个可序列化为JSON的对象。如果连class的实例对象都无法序列化为JSON，这肯定不合理！
    # 别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：https://docs.python.org/3/library/json.html#json.dumps
    # 这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
    # 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
    print(json.dumps(s, default=student2dict))  # {"name": "cjh", "age": 20, "score": 88}
    # 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict. 因为通常class的实例都有一个dict属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了slots的class
    print(json.dumps(s, default=lambda obj: obj.__dict__))  # {"name": "cjh", "age": 20, "score": 88}

    # 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))  # <__main__.Student object at 0x107e68e50>
