t = int(input())

for _ in range(t) :
  n, k = map(int, input().split())
  data = list(map(int, input().split()))
  result = 0
  for i in data :
    result += i // k

  print(result)
  
  
  # 승택이가 각 종류의 사탕을 몇 개 갖고 있는지 리스트 형태로 입력받고 반복문을 통해 data 리스트에 있는 값들을
  # 하나씩 확인하여 k로 나눈 몫을 result에 누적해나간다. 최종적으로 result값을 출력한다.
