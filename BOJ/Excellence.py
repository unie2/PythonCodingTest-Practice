n = int(input())
data = []
for _ in range(n) :
  data.append(int(input()))
data.sort()

min_value = 1000001
for i in range(n // 2) :
  value = data[i] + data[-(i+1)]
  min_value = min(min_value, value)

print(min_value)


# 1. 입력받은 n개의 정수를 입력받아 리스트 형태로 구성하고 오름차순으로 정렬한다.
# 2. n // 2 만큼의 범위를 지정하여 반복문을 수행하고, 내부에서는 먼저 data리스트의 가장 앞 원소와 가장 뒷 원소를 더하여 value에 할당한다.
# 3. 도출한 value값과 현재 저장되어 있는 최소값(min_value)을 비교하여 더 작은 값으로 min_value에 갱신한다.
# 4. 반복문이 종료되면 최종적으로 min_value를 출력한다.
