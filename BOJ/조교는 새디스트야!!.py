n = int(input())
data = list(map(int, input().split()))

result = 0
for i in range(1, n + 1) :
  if data[i-1] != i :
    result += 1

print(result)


# 1. 반복문의 범위는 1부터 n + 1로 지정하고, 내부에 조건문을 선언하여 data 리스트의 [i-1]번째 값과 i의 값이 일치하지 않는다면 번호 순서대로 서지 않은 사람이므로 result의 값을 1 증가시킨다.
# 2. 최종적으로 result의 값을 출력한다.
