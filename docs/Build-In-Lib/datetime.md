# datetime 时间处理



```python
from datetime import datetime

# 本地 当前时间 2019-01-13 00:36:52.957355
print(datetime.now())

# UTC 0 时区 的时间 2019-01-12 16:36:52.957405
print(datetime.utcnow())

# 2019-01-13
print(datetime.now().date())

# 00:43:36.884956
print(datetime.now().time())

# 1547311416884.9722
# 13 位的毫秒时间戳
print(datetime.now().timestamp() * 1000)

# 根据 13 位时间戳构建当地时间 2016-02-25 20:21:04
print(datetime.fromtimestamp(1456402864242 / 1000).strftime('%Y-%m-%d %H:%M:%S'))

# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=13, tm_hour=0, tm_min=43, tm_sec=36, tm_wday=6, tm_yday=13, tm_isdst=-1)
print(datetime.now().timetuple())

```



## 时间格式化

> 详见 官方文档 [strftime() and strptime()](https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior)

| Directive | Meaning                                                      | Example                                                      |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `%a`      | Weekday as locale’s abbreviated name.                        | Sun, Mon, …, Sat (en_US); So, Mo, …, Sa (de_DE)              |
| `%A`      | Weekday as locale’s full name.                               | Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE) |
| `%w`      | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. | 0, 1, …, 6                                                   |
| `%d`      | Day of the month as a zero-padded decimal number.            | 01, 02, …, 31                                                |
| `%b`      | Month as locale’s abbreviated name.                          | Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE)           |
| `%B`      | Month as locale’s full name.                                 | January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE) |
| `%m`      | 月份，`%M` 是分钟                                            | 01, 02, …, 12                                                |
| `%y`      | 年份                                                         | 00, 01, …, 99                                                |
| `%Y`      | 年份全称                                                     | 0001, 0002, …, 2013, 2014, …, 9998, 9999                     |
| `%H`      | 24小时制                                                     | 00, 01, …, 23                                                |
| `%I`      | 12小时制                                                     | 01, 02, …, 12                                                |
| `%p`      | AM 或 PM.                                                    | AM, PM (en_US); am, pm (de_DE)                               |
| `%M`      | 分钟，`%m` 是月份                                            | 00, 01, …, 59                                                |
| `%S`      | 秒                                                           | 00, 01, …, 59                                                |
| `%f`      | 微妙                                                         | 000000, 000001, …, 999999                                    |
| `%z`      | UTC offset in the form +HHMM or -HHMM (empty string if the object is naive). | (empty), +0000, -0400, +1030                                 |
| `%Z`      | Time zone name (empty string if the object is naive).        | (empty), UTC, EST, CST                                       |
| `%j`      | Day of the year as a zero-padded decimal number.             | 001, 002, …, 366                                             |
| `%U`      | Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, …, 53                                                |
| `%W`      | Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. | 00, 01, …, 53                                                |
| `%c`      | Locale’s appropriate date and time representation.           | Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE) |
| `%x`      | Locale’s appropriate date representation.                    | 08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE)      |
| `%X`      | Locale’s appropriate time representation.                    | 21:30:00 (en_US); 21:30:00 (de_DE)                           |
| `%%`      | A literal `'%'` character.                                   | %                                                            |



## Read More

- [极客学院 > Python 之旅 > datetime](http://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/datetime.html)
- 官方文档 [ datetime — Basic date and time types](https://docs.python.org/3.6/library/datetime.html)

