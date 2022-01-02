n = list(input())
n.insert(0, 'N')

result = 0
for i in range(1, len(n)) :
  if n[i] == 'Y' :
    for j in range(i, len(n), i) :
      if n[j] == 'Y' :
        n[j] = 'N'
      else :
        n[j] = 'Y'
    
    result += 1

print(result)


# 1. 인덱스를 편리하게 1번부터 확인하기 위해 입력받은 리스트 첫번째 요소에 'N'을 삽입한다.
# 2. 반복문을 통해 문자를 하나씩 확인하는데, 해당 인덱스의 문자가 'Y'일 경우 i의 배수 번호를 가지는 전구의 상태를 반전시킨다.
# 3. 하나의 인덱스 값을 확인할 때마다 result값을 1 증가시켜, 반복문이 모두 끝나면 최종적으로 result 값을 출력한다.
