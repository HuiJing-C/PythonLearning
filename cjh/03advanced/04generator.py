# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


if __name__ == '__main__':
    # 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
    print((x * x for x in range(1, 11)))  # <generator object <genexpr> at 0x10df9ef20>
    g = (x * x for x in range(1, 11))
    print(next(g))  # 1
    print(next(g))  # 4
    print(next(g))  # 9
    for n in (x * x for x in range(1, 11)):
        print(n)

    # generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
    # 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
    fib(10)
    # 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
    # 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    print(fib2(10))  # <generator object fib2 at 0x10456a580>

    # 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
    # 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    o = odd()
    next(o)  # step 1
    next(o)  # step 2
    next(o)  # step 3
    # next(o)  # StopIteration

    # 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
    # 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
    f = fib2(6)
    while True:
        try:
            x = next(f)
            print("f: ", x)
        except StopIteration as e:
            print("Generator return value: ", e.value)  # Generator return value:  done
            break
