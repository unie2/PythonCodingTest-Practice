import sys
input = sys.stdin.readline

data = list(input().rstrip())
temp = []

n = int(input())
for _ in range(n) :
    order = list(input().split())
    if order[0] == 'L' : # 커서를 왼쪽으로 한 칸 이동
        if data :
            temp.append(data.pop())
    elif order[0] == 'D' : # 커서를 오른쪽으로 한 칸 이동
        if temp :
            data.append(temp.pop())
    elif order[0] == 'B' : # 커서 왼쪽에 위치한 값 삭제
        if data :
            data.pop()
    elif order[0] == 'P' : # 커서 위치에 문자 추가
        data.append(order[1])

data.extend(reversed(temp))
print(''.join(data))

'''
1. 입력받은 order[0] 값이 'L'일 경우 아래와 같은 작업을 수행한다.
  - 만약 data 리스트에 값이 존재한다면 가장 마지막 요소를 빼내어 temp 리스트에 추가한다.

2. 입력받은 order[0] 값이 'D'일 경우 아래와 같은 작업을 수행한다.
  - 만약 temp 리스트에 값이 존재한다면 가장 마지막 요소를 빼내어 data 리스트에 추가한다.

3. 입력받은 order[0] 값이 'B'일 경우 아래와 같은 작업을 수행한다.
  - 만약 data 리스트에 값이 존재한다면 가장 마지막 요소를 빼낸다.

4. 입력받은 order[0] 값이 'P' 일경우 order[1] 문자를 data 리스트에 추가한다.

5. 최종적으로 temp 리스트의 값을 거꾸로 하여 data 리스트에 합친 후 문자들을 붙여 출력한다.

'''
