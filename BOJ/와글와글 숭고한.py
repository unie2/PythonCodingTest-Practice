s, k, h = map(int, input().split())

if s + k + h >= 100 :
  print('OK')
else :
  min_value = 100
  min_name = ""
  if min_value > s :
    min_value = s
    min_name = "Soongsil"
  if min_value > k :
    min_value = k
    min_name = "Korea"
  if min_value > h :
    min_value = h
    min_name = "Hanyang"

  print(min_name)
  
  
# 1. 조건문을 통해 숭실대학교의 참여도(s), 고려대학교의 참여도(k), 한양대학교의 참여도(h)의 합이 100 이상이라면 'OK'를 출력한다.
# 2. 그렇지 않다면 조건문을 통해 참여도가 가장 적은 대학교를 구하여 출력한다.
