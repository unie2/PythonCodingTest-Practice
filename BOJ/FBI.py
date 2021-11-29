data = []

for _ in range(5) :
  data.append(input())

flag = 0
for i in range(len(data)) :
  if 'FBI' in data[i] :
    print(i+1, end=' ')
    flag = 1

if flag == 0 :
  print('HE GOT AWAY!')
  
  
# 1. 5개의 요원 첩보원명을 입력받아 리스트에 추가한다.
# 2. 반복문을 통해 리스트에 존재하는 값을 하나씩 확인하여 현재 확인하는 값 중 'FBI' 단어가 존재할 경우 해당 인덱스 번호+1 을 출력하고 flag 값을 1로 갱신한다.
# 3. 반복 수행이 모두 끝나면 flag 값을 확인하여 그 값이 0이면 FBI 요원이 없기 때문에 "HE GOT AWAY!"를 출력한다.
