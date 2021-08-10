# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。
# 有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复bug。
# >>>   print()   <<<
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息

# >>>   assert   <<<
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。如果断言失败，assert语句本身就会抛出AssertionError
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert, 关闭后，你可以把所有的assert语句当成pass来看

# >>>   logging   <<<
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

# >>>   pdb   <<<
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
# python3 -m pdb err.py
# 输入命令n可以单步执行代码 (Pdb) n
# 任何时候都可以输入命令p 变量名来查看变量  (Pdb) p s(变量)
# 输入命令q结束调试，退出程序  (Pdb) q

# >>>   pdb.set_trace()  <<<
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行

# >>>   IDE   <<<
# 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm http://www.jetbrains.com/pycharm/
# 另外，Eclipse加上pydev插件也可以调试Python程序。

# 写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器
import logging

logging.basicConfig(level=logging.INFO)  # 不加这个没输出
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
if __name__ == '__main__':
    # assert 10 == 1
    logging.info("666")
