# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

if __name__ == '__main__':
    print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = []
    for x in range(1, 11):
        l.append(x * x)
    print(l)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
    print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    # 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法
    # for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
    print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]
    # 还可以使用两层循环，可以生成全排列：
    print([m + n for m in "ABC" for n in "DEF"])  # ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
    # 列表生成式也可以使用两个变量来生成list：
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print(["k=" + k + " v=" + v for k, v in d.items()])  # ['k=x v=A', 'k=y v=B', 'k=z v=C']
    print([v.lower() for v in d.values()])  # ['a', 'b', 'c']
