n = int(input())
arr = list(map(int, input().split()))
arr.sort() # 오름차순으로 정렬

target = 1
for i in arr :
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if target < i :
    break
  target += i

print(target)
