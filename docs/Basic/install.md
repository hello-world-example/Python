# 安装



## 下载安装

<https://www.python.org/downloads/>

<https://www.python.org/downloads/release/python-366/>



校验是否安装成功

```bash
python3 --version
# Python 3.6.6 

pip3 --version
# pip 18.1 from /Library/Frameworks/Python.framework/... (python 3.6)
```



> - [安装Python 3.7](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)



## virtualenv

在没有虚拟环境的情况下，`pip` 安装的第三方依赖，默认都会安装到 Python 的 `site-packages` 目录下，所有应用公用一套 Python 环境。使用 `virtualenv` 工具可以用来创建一套 **隔离** 的 Python 运行环境。

有时，不同的项目可能需要不同版本的 Python，但是如果都装到一起，经常会导致问题。所以需要一个工具能够将不同版本的环境隔离开来，需要哪个版本就切换到哪个版本做为默认版本。`virtualenv` 既是满足这个需求的工具。它能够用于创建独立的 Python 环境，多个Python 和第三方依赖 相互独立，互不影响。

```bash
# 安装 
pip3 install -U virtualenv

# 查看版本
virtualenv --version
# 16.2.0

# 创建 虚拟环境，使用 python3 创建虚拟环境，环境名是 venv-tf，执行成功后 会在当前目录下生成 venv-tf 文件夹
virtualenv --system-site-packages -p python3 ./venv-tf

# 激活，进入虚拟环境，进行重构后，shell 提示符前面会有 (venv-tf) 字样
source ./venv-tf/bin/activate

# 退出虚拟虚拟环境
(venv-tf) deactivate

# 删除虚拟环境，只需要删除创建的文件夹即可
rm -rf ./venv-tf

```



> - [Pip and virtualenv on Windows](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)
> - [python 虚拟环境设置](https://www.jianshu.com/p/44ab75fbaef2)



## 安装 TensorFlow 

```bash
# 首先进入虚拟环境
source ./venv-tf/bin/activate

# 安装 tensorflow
(venv-tf) xxx $ pip install --upgrade tensorflow

# 其他依赖
(venv-tf) xxx $ pip install numpy
(venv-tf) xxx $ pip install pandas
```

 

> 「官方文档」[使用 pip 安装 TensorFlow](https://www.tensorflow.org/install/pip)

## IDE 推荐

PyCharm Community Edition 免费社区版即可： https://www.jetbrains.com/pycharm/

社区版 和 专业版的区别是 没有 Web 开发的插件。



下载安装成功，创建项目的第一步，选择虚拟环境： **Project Interpreter** > **Existing interpreter** > 选择 `venv-tf/bin/python3`；

也可以在创建项目成功后，打开 **Preferences** > **Project** >  **Project Interpreter**，选择指定的虚拟环境。

PyCharm 可以非常方便的 查看 和 管理 虚拟环境的中的 第三方依赖。

## 其它工具

- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html) 管理虚拟环境
- [ipython](http://ipython.org/) 强大的 Python 交互式 Shell 
- [Jupyter Notebook](https://jupyter.org/) 在线编写 Python 脚本 等，内核是 ipython