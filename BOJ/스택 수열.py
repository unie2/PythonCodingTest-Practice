n = int(input())
count = 0
stack = []
result = []
flag = True

for _ in range(n) :
    data = int(input())
    while count < data :
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == data :
        stack.pop()
        result.append('-')
    else :
        flag = False
        break

if flag == False :
    print("NO")
else :
    print('\n'.join(result))
    
'''
1. n개의 수를 입력받는데, 현재의 count 값이 입력받은 값(data) 이상이 될 때까지 아래와 같은 작업의 while문을 수행한다.
  - count를 1 증가시킨다.
  - stack 리스트에 count 값을 추가하고, result에 '+' 를 추가한다.

2. 만약 stack리스트의 가장 마지막 요소와 data가 같을 경우 stack의 마지막 요소를 빼내고 result 리스트에 '-'를 추가한다.

3. 그렇지 않을 경우 flag를 False로 갱신하고 break 한다.

4. 최종적으로 flag값을 확인하여 그 값이 False라면 "NO"를 출력하고, True라면 한 줄에 한 개씩 result 리스트의 요소를 출력한다.

'''
