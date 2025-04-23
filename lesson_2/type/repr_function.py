# repr() vs str()
import datetime as date

# repr()
x = [1, 2, 3]
repr_x = repr(x)
print(repr_x)   # [1, 2, 3]

today = date.datetime.now()
print(str(today))
# 2025-04-17 15:31:35.683456
print(repr(today))
# datetime.datetime(2025, 4, 17, 15, 31, 55, 705527)
repr_today = date.datetime(2025, 4, 17, 15, 31, 55, 705527)
print(repr_today)
# 2025-04-17 15:31:55.705527
print(str(today))