n = int(input())

data = []

for _ in range(n) :
  value = input()
  data.append(value)

state = int(input())

if state == 1 :
  for i in range(len(data)) :
    print(data[i])
elif state == 2 :
  for i in range(len(data)) :
    print(data[i][::-1])
else :
  for i in range(len(data)-1, -1, -1) :
    print(data[i])
    
    
# 1. n개의 문자열을 입력받아 리스트형태로 구성한다.
# 2. 입력받은 마법거울의 심리상태(state)가 1이라면 지영 공주님의 모습을 있는 그대로 표현한다.
# 3. 입력받은 마법거울의 심리상태(state)가 2라면 좌/우 반전된 모습을 출력한다.
# 4. 입력받은 마법거울의 심리상태(state)가 3이라면 상/하로 반전된 모습을 출력한다.
