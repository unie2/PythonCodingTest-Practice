s = input()
data = ['U', 'C', 'P', 'C']
flag = True

for i in range(4) :
  if data[i] in s :
    flag = True
    index = s.find(data[i])
    s = s[index+1::]
  else :
    flag = False
    break

if flag == True :
  print('I love UCPC')
else :
  print('I hate UCPC')
  
  
# 1. UCPC가 입력받은 문자열의 줄임말인지를 확인하기 위해 data리스트에 'U', 'C', 'P', 'C'를 저장한다.
# 2. 반복문을 통해 data 리스트의 값을 하나씩 확인하면서 해당 문자가 입력받은 문자열(s)에 있는지 확인한다.
# 3. 있다면 flag값을 True로 갱신하고 s 문자열에서 해당 문자가 있는 인덱스 번호를 가져와 그 인덱스부터의 문자열을 다시 s에 갱신한다.
# 4. 없다면 flag 값을 False로 갱신하고 반복문을 종료시킨다.
# 5. 최종적으로 flag값을 확인하여 그 값이 True라면 'I love UCPC'를 출력하고, False라면 'I hate UCPC'를 출력한다.
