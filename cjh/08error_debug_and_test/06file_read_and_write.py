if __name__ == '__main__':
    # 标示符'r'表示读
    f = open("test", 'r')
    # 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    print(f.read())  # Hello World, CJH nb plus
    f.close()
    try:
        f2 = open("test2", 'r')
        print(f2.read())
        f2.close()
    except FileNotFoundError as e:
        print("Error")

    # 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
    with open('test', 'r') as f:
        print(f.read())

    # 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了
    # 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
    # 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
    # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便

    # >>>   file-like Object   <<<
    # 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
    # StringIO就是在内存中创建的file-like Object，常用作临时缓冲

    # >>>   二进制文件   <<<
    # 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
    with open('test', 'rb') as f3:
        print(f3.read())  # b'Hello World, CJH nb plus'

    # >>>   字符编码   <<<
    # 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取utf-8编码的文件
    with open('test', 'r', encoding='utf-8') as f4:
        print(f4.read())  # Hello World, CJH nb plus

    # 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
    # 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
    with open('test', 'r', encoding='gbk', errors='ignore') as f5:
        print(f5.read())  # Hello World, CJH nb plus

    # >>>   写文件   <<<
    # 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
    with open('test2', 'w') as f6:
        f6.write("It's a test")
