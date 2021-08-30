# datetime是Python处理日期和时间的标准库。
from datetime import datetime, timedelta, timezone

if __name__ == '__main__':
    # 获取当前日期和时间
    print(datetime.now())  # 2021-08-30 16:08:15.433189
    # 获取指定日期和时间
    print(datetime(2021, 8, 30, 16, 14, 10, 123))  # 2021-08-30 16:14:10.000123, 不填的值按0计算
    # datetime转换为timestamp 注：时间戳不分时区
    print(datetime.now().timestamp())  # 1630311558.84324 注意Python的timestamp是一个浮点数。小数位之前是秒，之后是毫秒。
    # timestamp转换为datetime
    print(datetime.fromtimestamp(1630311558.84324))  # 2021-08-30 16:19:18.843240
    # datetime是有时区的。上述转换是在timestamp和本地时间做转换。timestamp也可以直接被转换到UTC标准时区的时间
    print(datetime.utcfromtimestamp(1630311558.84324))  # 2021-08-30 08:19:18.843240
    # str转换为datetime
    print(datetime.strptime('2021-08-30 16:19:18', '%Y-%m-%d %H:%M:%S'))  # 2021-08-30 16:19:18 注意转换后的datetime是没有时区信息的
    # 时间格式参见：https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    # datetime转换为str
    print(datetime.now().strftime('%a, %b %d %H:%M'))  # Mon, Aug 30 16:29
    # datetime加减
    print(datetime.now() - timedelta(days=1))
    print(datetime.now() + timedelta(days=-1))
    # 本地时间转换为UTC时间
    # 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
    # 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
    tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
    now = datetime.now()
    dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区
    print(dt)  # 2021-08-30 17:20:57.903955+08:00
    # 时区转换
    # 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)  # 2021-08-30 09:23:08.349803+00:00
    # astimezone()将转换时区为北京时间:
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)  # 2021-08-30 17:24:16.116040+08:00
    # astimezone()将bj_dt转换时区为东京时间:
    tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)  # 2021-08-30 18:25:13.115330+09:00
    # 不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换

    # 小结
    # datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
    # 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
