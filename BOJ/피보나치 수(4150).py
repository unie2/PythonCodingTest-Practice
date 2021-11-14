n = int(input())

data = [0, 1, 1]
for i in range(3, n + 1) :
  data.append(data[i-1] + data[i-2])

print(data[n])


# 1. 반복문을 통해 3번째 인덱스부터 n번째 인덱스까지 각 피보나치 수열 값을 추가한다.
# 2. 최종적으로 입력받은 정수에 해당하는 피보나치 수를 출력한다.
