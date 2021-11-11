data = []

while True :
  n = float(input())
  if n == 999 :
    break
  data.append(n)

for i in range(1, len(data)) :
  print("%.2f" % (data[i] - data[i - 1]))
  
  
# 1. 값을 입력받아 data 리스트에 추가한다.
# 2. 입력받은 값이 999일 경우 반복문을 종료한다.
# 3. for문을 통해 data리스트 1번째 요소부터 끝까지 범위를 지정하여 값을 하나씩 확인한다.
# 4. 해당 인덱스의 값에서 이전 인덱스의 값을 빼고 소수점 둘째자리까지 출력한다.
