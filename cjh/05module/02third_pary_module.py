# 使用交互式命令时，如果所属的模块没加载上来，出现以下错误，可以采用以下几种方式解决
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named ***

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中，获取：sys.path
# 一：直接修改sys.path，添加要搜索的目录 sys.path.append('/Users/cjh/Desktop')  这种方法是在运行时修改，运行结束后失效。
# 二：第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

# 使用交互式命令时，如果import时出现这个错误：SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# python交互式命令不允许使用数字开头的源文件，要把数字开头的数字删掉

# 安装用python自带pip命令 pip install *** 安装第三方模块
