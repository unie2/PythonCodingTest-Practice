n = int(input())

for _ in range(n) :
  data = list(input().split())
  for i in range(2, len(data)) :
    print(data[i], end=' ')
  
  print(data[0], data[1])
  
  
# 1. 문자열을 입력받아 리스트 형태로 구성한다.
# 2. 반복문을 통해 가장 앞 단어 두 개 이후의 단어들을 출력하고, 반복문이 끝나면 가장 앞 단어 두 개를 출력한다.
