from bisect import bisect_left, bisect_right

def count(arr, left_value, right_value) :
  right_index = bisect_right(arr, right_value)
  left_index = bisect_left(arr, left_value)
  return right_index - left_index

n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = count(arr, x, x)

if result != 0 :
  print(result)
else :
  print(-1)
