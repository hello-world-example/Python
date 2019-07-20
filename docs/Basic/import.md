# import 机制

## 简介

**module**：用来从逻辑上组织 Python 代码，如：变量、函数、类，**本质就是`*.py`文件**

**package**：定义了一个由 模块 和 子包 组成的 Python 应用程序执行环境，**本质就是一个有层次的文件目录结构**，必须带有一个 `__init__.py`文件 



## 导入方法

```
# 导入一个模块
import model_name [as new_name]

# 导入多个模块
import module_name1,module_name2

# 导入模块中的指定的属性、方法（不加括号）、类
from moudule_name import moudule_element [as new_name]
```



## Read More

- [Python中import机制](https://www.cnblogs.com/yan-lei/p/7828871.html)