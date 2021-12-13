n = int(input())
data = list(map(int, input().split()))

index = 0
for i in range(len(data)) :
  if data[i] == -1 :
    index = i
    break

print(min(data[:index:]) + min(data[index+1::]))


# 1. 펭귄이 위치한 인덱스를 기준으로 왼쪽 부분 중 최솟값과 오른쪽 부분 중 최솟값을 더하여 문제를 해결할 수 있다.
# 2. 얼음을 깨뜨리는 데에 드는 힘을 의미하는 수를 입력받아 리스트 형태로 구성하여 data에 저장한다.
# 3. 반복문을 통해 data 리스트의 값을 하나씩 확인하여 해당 값이 -1일 경우 index에 해당 인덱스 값을 저장한다.
# 4. 저장된 index 값을 기준으로 왼쪽 부분의 최솟값과 오른쪽 부분의 최솟값을 더하여 출력한다.
