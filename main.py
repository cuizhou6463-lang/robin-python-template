# -*- coding: utf-8 -*-
"""
Robin's Daily Utilities
一些日常用的小工具
"""

import datetime

def hello(name="World"):
    """打招呼"""
    print(f"Hello, {name}!")

def today():
    """打印今天的日期"""
    print(f"今天是: {datetime.date.today()}")

def days_until(date_str):
    """计算距离某天还有多少天，格式: YYYY-MM-DD"""
    target = datetime.date.fromisoformat(date_str)
    delta = target - datetime.date.today()
    print(f"距离 {date_str} 还有 {delta.days} 天")

if __name__ == "__main__":
    hello("Robin")
    today()
    print("---")
    print("用法:")
    print("  hello(name)      - 打招呼")
    print("  today()          - 今天的日期")
    print("  days_until(date)- 计算倒计时，格式 YYYY-MM-DD")
