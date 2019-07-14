# `__future__`



Python 3 引入了一些与 Python 2 不兼容的关键字和特性，在 Python 2 中，可以通过内置的 `__future__ `模块导入这些新内容。如果你希望在 Python 2 环境下写的代码也可以在 Python 3 中运行，那么建议使用`__future__`模块。

即Python提供的`__future__`模块，可以把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。



## print_function

```python
from __future__ import print_function
import sys

# 这样 Python2.7 环境下的代码也可以在 Python3.0 以上版本中运行了！
print('error happens!', file=sys.stderr)

```



## unicode_literals

在 Python 2.7 版本中运行以下代码

```python
from __future__ import unicode_literals


# 'xxx' is unicode? True
print '\'xxx\' is unicode?', isinstance('xxx', unicode)

# u'xxx' is unicode? True
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)

# 'xxx' is str? False
print '\'xxx\' is str?', isinstance('xxx', str)

# b'xxx' is str? True
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
```



## Read More

- [python 中的`__futrue__`模块，以及unicode_literals模块](https://www.cnblogs.com/ccorz/p/python-zhong-defutruemo-kuai-yi-jiunicodeliterals-.html)
- 