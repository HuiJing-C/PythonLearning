# 为了编写单元测试，我们需要引入Python自带的unittest模块
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码
# if __name__ == '__main__':
#     unittest.main()
# 这样就可以把xxx.py当做正常的python脚本运行

# 另一种方法是在命令行通过参数-m unittest直接运行单元测试  python3 -m unittest mytest
# 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。

# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
import unittest


class TestOne(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    def test_one(self):
        self.assertEqual(1, 1)
        # 待抛出指定类型的Error
        with self.assertRaises(ZeroDivisionError):
            value = 10 / 0
            print(value)

    def test_two(self):
        print("777")


if __name__ == '__main__':
    unittest.main()
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
#
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
#
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
#
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。