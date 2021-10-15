a, b, c = map(int, input().split())
d = int(input())

get_seconds = (c + d) % 60
get_minute = (c + d) // 60

result_minute = (b + get_minute) % 60
get_hour = (b + get_minute) // 60

result_hour = (a + get_hour) % 24

print(result_hour, result_minute, get_seconds)
