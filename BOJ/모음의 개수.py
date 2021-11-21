data = input()
result = 0

for i in range(len(data)) :
  if data[i] == 'a' or data[i] == 'e' or data[i] == 'i' or data[i] == 'o' or data[i] == 'u' :
    result += 1

print(result)


# 1. 단어를 입력받아 반복문을 통해 문자를 하나씩 확인하여 해당 문자가 모음이라면 result 값을 1 증가 시킨다.
# 2. 최종적으로 모음의 개수 즉, result 값을 출력한다.
