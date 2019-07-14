# 字典 dict

> 本文来自：
>
> - [python字典遍历的几种方法 ](https://www.cnblogs.com/stuqx/p/7291948.html)
> - [Python中如何高效的创建字典](https://blog.csdn.net/mmayanshuo/article/details/79205641)

## 创建

TODO

## 遍历

### 示例数据

```python
map = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
```

### 遍历key值

```python
for key in map:
    print(key, ':', map[key])
```

等价于：

```python
for key in map.keys():
    print(key, ':', map[key])
```

### 遍历value值

```python
for value in map.values():
    print(value)
```

### 遍历字典项

```python
for item in map.items():
    print(item)
```

输出：

```python
('a', 1)
('b', 2)
('c', 3)
('d', 4)
```

### 遍历字典健值

遍历 `map.items()` 的时候，每一项是元组，所以也可以通过两个变量来接收

```python
for key, value in map.items():
    print(key, ':', value)
```



