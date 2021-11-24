import datetime

data = datetime.datetime.now() + datetime.timedelta(hours=9)

print(data.year)
print(data.month)
print(data.day)


# 1. datetime을 통해 현재의 시간을 가져오는데, 한국 시간으로 가져오기 때문에 9시간을 더해준다.
# 2. 최종적으로 연도, 월, 일을 하나씩 순서대로 출력한다.
