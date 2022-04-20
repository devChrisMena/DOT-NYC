from datetime import datetime, timedelta
from ast import Tuple

post = ('Christopher', 'Message', '2022-04-20')
x = datetime.now() - timedelta(days=10)
dt = post[2]
print(dt[:4])
print(dt[5:7])
print(dt[8:])

p_date = datetime(int(dt[:4]), int(dt[5:7]), int(dt[8:]))
print(p_date)
t = x > p_date
print(t)