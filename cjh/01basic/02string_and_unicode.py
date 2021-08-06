if __name__ == '__main__':
    # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
    print(ord("辉"), chr(36745))  # 36745 辉
    print('\u4e2d\u6587')  # 中文 -> 十六进制写法
    # Python对bytes类型的数据用带b前缀的单引号或双引号表示：
    print(b"ABC"[0])  # 65
    # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
    # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错:UnicodeEncodeError
    # 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
    print('ABC'.encode('ascii'))  # b'ABC'
    print("中文".encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
    # bytes变str要用decode()
    print(b'ABC'.decode('ascii'))  # ABC
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
    print(len("中文"))  # 2
    # 格式化字符串 整数%d 浮点数%f 字符串%s 十六进制整数%x, %s永远适用。格式化整数和浮点数还可以指定是否补0和整数与小数的位数
    print("%s %05d %.2f" % ("cjh", 18, 3.1415926))  # cjh 00018 3.14
