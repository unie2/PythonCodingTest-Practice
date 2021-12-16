n = int(input())
data = [0] * 1000001

for i in list(map(int, input().split())) :
  data[i] += 1

result = 0
for i in list(map(int, input().split())) :
  if data[i] >= 1 :
    data[i] -= 1
  else :
    result += 1

print(result)


# 1. 신청한 수업을 의미하는 수들을 입력받아 리스트 형태로 구성하고 반복문을 통해 data리스트의 해당 인덱스의 값을 1 증가시킨다.
# 2. 교환을 통해 수강하고 싶은 수업의 번호를 의미하는 수들을 입력받아 리스트 형태로 구성하고 반복문을 통해 값을 하나씩 확인한다.
# 3. 만약 data 리스트의 해당 인덱스의 값이 1이상일 경우 그 값을 1씩 빼준다.
# 4. 인덱스의 값이 0일 경우 result값을 1 증가시키고, 반복문이 종료되면 result 값을 출력한다.
