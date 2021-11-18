diction = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

value = ""
result = 0

for i in range(3) :
  s = input()
  if i != 2 :
    value += str(diction.get(s))
  else :
    result = int(value) * int('1' + ('0' * diction.get(s)))

print(result)


# 1. 문제에서 제시한 저항의 값들을 딕셔너리 형태로 구성한다.
# 2. 반복문을 통해 처음 색 2를 입력받아 각각 딕셔너리에서 value 값을 꺼내와 문자열 형태로 value에 추가한다.
# 3. 마지막에 입력받은 색은 곱해야 하므로, 우선 문자 1에 value값만큼 0을 추가하여 정수형으로 변환한 뒤 정수형 value에 곱한 값을 result에 할당한다.
# 4. 최종적으로 result 값을 출력한다.
