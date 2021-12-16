while True :
  try :
    s, t = input().split()
    
    value = 0
    flag = 0
    for i in range(len(t)) :
      if t[i] == s[value] :
        value += 1
        if value == len(s) :
          flag = 1
          break

    if flag == 1 :
      print('Yes')
    else :
      print('No')

  except :
    break
    
    
# 1. 입력받은 t의 문자열 길이만큼 범위를 지정하여 반복문을 수행하고, 내부에서는 조건문을 통해 현재 확인하고 있는 문자열 t의 문자와 지정된 s의 문자를 비교하여 같다면 s의 인덱스 값을 1 증가시킨다.
# 2. 만약 value의 값과 s의 문자열 길이가 같을 경우 부분 문자열에 해당되므로 flag를 1로 갱신한다.
# 3. 반복문이 종료되면 flag 값을 확인하고, 그 값이 1이면 'Yes'를, 0이라면 'No'를 출력한다.
