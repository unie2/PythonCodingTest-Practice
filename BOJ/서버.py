n, T = map(int, input().split())
data = list(map(int, input().split()))

count = 0
result = 0
for i in data :
  if count + i <= T :
    count += i
    result += 1
  else :
    break

print(result)


# 각 일의 수행 시간을 리스트 형태로 입력받고 반복문을 통해 data 리스트에 담겨 있는 값을 하나씩 확인한다.
# 반복문 내에서는 조건문을 통해 count + 현재 확인하고 있는 값(i)이 입력받은 T보다 작거나 같을 경우
# count에 현재 확인하고 있는 값을 누적하고 result 값을 1 증가시킨다.
# 만약 T보다 크기가 커질 경우 그 해당 값부터 그 이후의 값들까지 수행할 수 없기 때문에 break문을 통해 반복문을 종료한다.
# 최종적으로 result값을 출력한다.
