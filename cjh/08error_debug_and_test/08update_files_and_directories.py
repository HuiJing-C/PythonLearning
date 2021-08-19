# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令
# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数

import os
import shutil

if __name__ == '__main__':
    print(os.name)
    # 环境变量
    print(os.environ)
    # 取环境变量
    print(os.environ.get('endpoint', '666'))
    #  》》》》》》》操作文件和目录《《《《《《《《
    #  操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下
    #  查看当前目录的绝对路径
    print(os.path.abspath('.'))
    #  在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    #  把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下用/ 在Windows下用\
    #  同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
    print(os.path.split('/Users/cjh/Desktop/Python/PythonLearning/cjh/08error_debug_and_test'))  # ('/Users/cjh/Desktop/Python/PythonLearning/cjh', '08error_debug_and_test')
    print(os.path.join('/Users/cjh/Desktop/Python/PythonLearning/cjh/08error_debug_and_test', 'tesetdir'))
    #  新建
    os.mkdir(os.path.join('/Users/cjh/Desktop/Python/PythonLearning/cjh/08error_debug_and_test', 'tesetdir'))
    #  删除
    os.rmdir(os.path.join('/Users/cjh/Desktop/Python/PythonLearning/cjh/08error_debug_and_test', 'tesetdir'))

    # 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
    # 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
    # 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    # 列出所有.py文件
    print([x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py'])
