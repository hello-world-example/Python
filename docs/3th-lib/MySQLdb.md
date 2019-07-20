# MySQLdb



## Windows

```bash
pip install mysql-python
```

### 异常处理

#### error: Microsoft Visual C++ 9.0 is required

根据提示 访问 http://aka.ms/vcpython27 下载包安装

#### fatal error C1083: Cannot open include file: 'config-win.h': No such file or directory

1. 安装 wheel : `pip install wheel`
2. 下载 64位的 MySQL-Python： https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
3. 安装 `.whl` 文件 : `pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl`