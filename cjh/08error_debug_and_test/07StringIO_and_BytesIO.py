# 很多时候，数据读写不一定是文件，也可以在内存中读写
# StringIO顾名思义就是在内存中读写str
from io import StringIO
from io import BytesIO

if __name__ == '__main__':
    print("start")
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world')
    print(f.getvalue())  # hello world
    # 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
    f2 = StringIO('Hello\nHi\nGoodBye!')
    while True:
        s = f2.readline()
        if s == '':
            break
        print(s.strip())

    # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO. BytesIO实现了在内存中读写bytes
    b = BytesIO()
    b.write("中文".encode("utf-8"))
    print(b.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'
    b2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(b2.read())
