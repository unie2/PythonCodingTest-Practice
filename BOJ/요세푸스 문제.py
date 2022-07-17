n, k = map(int, input().split())
data = [i for i in range(1, n + 1)]

index = 0
result = []
for _ in range(n) :
    index += (k - 1)
    if index >= len(data) :
        index %= len(data)
    result.append(str(data[index]))
    data.pop(index)

print('<', end='')
print(', '.join(result), end='')
print('>')

'''
1. 1부터 n까지의 수를 data 리스트에 저장한다.

2. index를 0으로 초기화한 후 입력받은 n번만큼 아래 작업을 반복한다.
  - index에 (k - 1) 값을 누적한다.
  - 만약 누적된 index 값이 현재 data 리스트의 길이 이상일 경우 길이로 나눈 나머지 값으로 갱신한다.
  - result 리스트에 문자형으로 변환된 data[index] 값을 추가하고, 그 값을 pop()하여 빼낸다.

3. 최종적으로 result 리스트에 담겨 있는 값을 문제에서 요구하는 출력 형식에 맞추어 출력한다.

'''
