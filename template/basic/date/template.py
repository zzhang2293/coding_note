import time
from datetime import datetime, timedelta, date

"""
时间日期处理
"""


class DateTime:
    def __init__(self):
        self.leap_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.not_leap_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return

    @staticmethod
    def day_interval(year1, month1, day1, year2, month2, day2):
        """计算两个日期之间的天数"""
        date1 = date(year1, month1, day1)
        date2 = date(year2, month2, day2)
        return (date1 - date2).days

    @staticmethod
    def time_to_unix(dt: str) -> int:
        """
        时间字符串转换为 unix 时间戳
        example: "2019-10-15 00:00:00" -> 1571078400
        """
        time_array = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # for example: dt = "2019-10-15 00:00:00"
        return int(time.mktime(time_array))

    @staticmethod
    def unix_to_time(timestamp: int) -> str:
        """
        unix 时间戳转换为时间字符串
        example: 1571078400 -> "2019-10-15 00:00:00"
        """
        time_array = time.localtime(timestamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_array)

    @staticmethod
    def is_leap_year(self, yy):
        assert sum(self.leap_month) == 366  # 闰年 leap year
        assert sum(self.not_leap_month) == 365  # 平年 common year
        return yy % 400 == 0 or (yy % 4 == 0 and yy % 100 != 0)

    @staticmethod
    def get_n_days(yy, mm, dd, n):
        """the day of after n days from yy-mm-dd"""
        now = datetime(yy, mm, dd, 0, 0, 0, 0)
        delta = timedelta(days=n)
        n_days = now + delta
        return n_days.strftime("%Y-%m-%d")

    @staticmethod
    def is_valid_date(date_str):
        try:
            date.fromisoformat(date_str)
        except ValueError as _:
            return False
        else:
            return True

    def all_palindrome_date(self):
        """brute all the palindrome date from 1000-01-01 to 9999-12-31"""
        ans = []
        for y in range(1000, 10000):
            yy = str(y)
            mm = str(y)[::-1][:2]
            dd = str(y)[::-1][2:]
            if self.is_valid_date(f"{yy}-{mm}-{dd}"):
                ans.append(f"{yy}-{mm}-{dd}")
        return ans

    def unix_minute(self, s) -> int:
        """minutes start from 0000-00-00-00:00"""
        lst = s.split("-")
        y, m, d = [int(w) for w in lst[:-1]]
        h, minute = [int(w) for w in lst[-1].split(":")]
        day = d + 365 * y + self.leap_year_count(y)
        if self.is_leap_year(y):
            day += sum(self.leap_month[:m - 1])
        else:
            day += sum(self.not_leap_month[:m - 1])
        res = day * 24 * 60 + h * 60 + minute
        return res

    def unix_day(self, s: str) -> int:
        """days start from 0000-00-00-00:00"""
        lst = s.split("-")
        y, m, d = [int(w) for w in lst[:-1]]
        h, minute = [int(w) for w in lst[-1].split(":")]
        day = d + 365 * y + self.leap_year_count(y)
        if self.is_leap_year(y):
            day += sum(self.leap_month[:m - 1])
        else:
            day += sum(self.not_leap_month[:m - 1])
        res = day * 24 * 60 + h * 60 + minute
        return res // (24 * 60)

    def unix_second(self, s):
        """seconds start from 0000-00-00-00:00"""
        lst = s.split("-")
        y, m, d = [int(w) for w in lst[:-1]]
        h, minute, sec = [int(w) for w in lst[-1].split(":")]
        day = d + 365 * y + self.leap_year_count(y)
        if self.is_leap_year(y):
            day += sum(self.leap_month[:m - 1])
        else:
            day += sum(self.not_leap_month[:m - 1])
        res = (day * 24 * 60 + h * 60 + minute) * 60 + sec
        return res

    @staticmethod
    def leap_year_count(y):
        """leap years count small or equal to y"""
        return 1 + y // 4 - y // 100 + y // 400

    @staticmethod
    def get_start_date(year: int, month: int, day: int, hh, mm, ss, delta: int):
        """the time after any seconds"""
        start_date = datetime(year=year, month=month, day=day, hour=hh, minute=mm, second=ss)
        end_date = start_date + timedelta(seconds=delta)
        ans = [end_date.year, end_date.month, end_date.day, end_date.hour, end_date.minute, end_date.second]
        return ans
