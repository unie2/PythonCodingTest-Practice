n = int(input())
data = []

for _ in range(n) :
  data.append(int(input()))

value = data[-1] 
if data[2] - data[1] == data[1] - data[0] :
  value += data[2] - data[1] 
else :
  value *= data[2] // data[1]

print(value)


# 1. n개의 수들을 입력받아 리스트 형태로 구성한다.
# 2. value에 data 리스트에서 가장 마지막에 들어간 값을 할당한다.
# 3. 조건문을 통해 data리스트의 각 요소들 간의 차를 구하여 두 값이 같다면 등차수열로 판단 되어 value에 요소 간의 차를 더한다.
# 4. 그렇지 않을 경우 등비수열로 판단 되어 value에 data[2] // data[1] 의 값을 곱한다.
