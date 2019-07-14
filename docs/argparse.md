# argparse



> 官方文档 [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)
>
> 本文来自 [极客学院 > Python 之旅 > argparse](http://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/argparse.html)



`argparse` 是 Python 内置的一个**用于命令项选项与参数解析的模块**，通过在程序中定义好我们需要的参数，`argparse` 将会从 `sys.argv` 中解析出这些参数，并**自动生成帮助和使用信息**。


## 示例
使用的时候主要分一下三步：
- 创建 ArgumentParser() 对象
- add_argument() 添加参数
- parse_args() 解析参数

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--numA', help='参数1', required=True, type=int)
parser.add_argument('--numB', help='参数2', default=0, type=int)

args = parser.parse_args()

print("{} + {} = {}".format(args.numA, args.numB, args.numA + args.numB))
```

### 测试 运行结果

```bash
$ python test.py
usage: test.py [-h] --numA NUMA [--numB NUMB]
test.py: error: the following arguments are required: --numA

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

$ python test.py -h
usage: test.py [-h] --numA NUMA [--numB NUMB]

optional arguments:
  -h, --help   show this help message and exit
  --numA NUMA  参数1
  --numB NUMB  参数2
 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

$ python test.py --numA=1 
1 + 0 = 1

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

$ python test.py --numA=1 --numB=2
1 + 2 = 3

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

$ python test.py --numA=1 --NUMB=2
usage: test.py [-h] --numA NUMA [--numB NUMB]
test.py: error: unrecognized arguments: --NUMB=2

```



## add_argument() 

add_argument() 方法定义如何解析命令行参数：

```python
ArgumentParser.add_argument(
    # ❤ 选项字符串的名字或者列表，例如 foo 或者 -f, --foo
    name or flags...
    # ❤ 不指定参数时的默认值
    [, default]
    # ❤ 参数是否必传
    [, required]
    # ❤ 参数的帮助信息
    [, help]
    
    [, action]
    [, nargs]
    [, const]
    # 命令行参数应该被转换成的类型
    [, type]
    # 参数可允许的值
    [, choices]
    [, metavar]
    # 解析后的参数名称
    [, dest]
)
```



## parse_known_args()

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--numA', help='参数1', required=True, type=int)
parser.add_argument('--numB', help='参数2', default=0, type=int)

# FLAGS 是匹配到的参数
# args 保存未匹配到的参数
FLAGS, args = parser.parse_known_args()

print("{} + {} = {}".format(FLAGS.numA, FLAGS.numB, FLAGS.numA + FLAGS.numB))

print("未解析的参数", args)

```

### 测试 运行结果

```bash
# args = parser.parse_args() 的形式会直接报错 
# FLAGS, args = parser.parse_known_args() 会把为匹配到的 保存在 args 变量里
$ python test.py --numA=1 --NUMB=2
1 + 0 = 1
未解析的参数 ['--NUMB=2']
```



## Read More

- [Parsing boolean values with argparse](https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse)

