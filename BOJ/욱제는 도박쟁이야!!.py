n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = 0
for i in range(len(first)) :
  result += abs(first[i])

for i in range(len(second)) :
  result += abs(second[i])

print(result)


# 1. 욱제의 첫 번째 라운드, 두 번째 라운드의 n개의 동전을 입력받아 각 리스트 형태로 구성한다.
# 2. 결국 두 라운드의 절대값의 합을 구해야하므로 반복문을 통해 각 수의 절대값을 result에 누적한다.
# 3. 최종적으로 result 값을 출력한다.
