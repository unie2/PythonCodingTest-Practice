s = input()

sum_value = 0
for i in range(len(s)) :
  if ord(s[i]) >= 97 :
    sum_value += int(ord(s[i]) - 96)
  else :
    sum_value += int(ord(s[i]) - 38)

flag = 0
for i in range(2, int(sum_value**0.5) + 1) :
  if sum_value % i == 0 :
    flag = 1

if flag == 0 :
  print("It is a prime word.")
else :
  print("It is not a prime word.")
  
  
# 1. 반복문을 통해 입력받은 문자열의 문자를 하나씩 확인하고, 그 값이 아스키코드 값으로 97이상일 경우 소문자에
# 해당하기 때문에 96을 뺀 값을 정수형으로 sum_value에 누적한다.
# 만약 97 미만일 경우 대문자에 해당하기 때문에 38을 뺀 값을 정수형으로 sum_value에 누적한다.
# 2. 반복문을 통해 단어의 합을 의미하는 sum_value가 소수인지 판별할 수 있도록 하고, 소수라면 flag값을 1로 갱신한다.
# 3. 최종적으로 flag값을 확인하여 문제에서 요구하는 출력 형식으로 문자열을 촐력한다.
