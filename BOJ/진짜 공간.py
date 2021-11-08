n = int(input())
data = list(map(int, input().split()))
cluster = int(input())

result = 0
for i in data :
  if i % cluster > 0 :
    result += i // cluster + 1
  else :
    result += i // cluster

print(cluster * result)


# n개의 파일 크기를 리스트 형태로 입력받아 구성하여 반복문을 통해 data 리스트 내에 있는 값을 하나씩 확인한다.
# 반복문 내에서는 조건문을 통해 현재 확인하고 있는 값을 입력받은 클러스터의 크기(cluster)로 나눈 나머지 값이
# 0보다 클경우 하나의 클러스터를 더 사용해야 하기 때문에 몫에 1을 더하여 result에 누적한다.
# 0 이하일 경우 하나의 클러스터를 더 사용할 필요가 없기 때문에 단순히 몫만 result에 누적한다.
# data 리스트에 담겨있는 값을 모두 확인한 뒤 반복문이 끝나면 최종적으로 클러스터 크기에 result 값을 곱하여 출력한다.
