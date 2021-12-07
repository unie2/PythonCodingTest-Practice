while True :
  n = input()
  if n == '#' :
    break
  value = n[0]
  data = n[2::]
  result = data.count(value) + data.count(value.upper())
  print(value, result)
  
  
# 1. 입력받은 값이 '#'일 때까지 반복 수행한다.
# 2. value에 입력받은 n의 0번째 문자 즉, 몇 번 나타나는지를 세려고 하는 알파벳을 담는다.
# 3. data에 2번째부터 끝까지의 문자열을 담는다.
# 4. data 문자열에서 소문자 알파벳과 대문자 알파벳의 개수를 구하여 더한 뒤 result에 할당한다.
# 5. 최종적으로 문제에서 요구하는 출력형식과 같이 해당 알파벳과 개수를 출력한다.
