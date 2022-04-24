r, c, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]

time = 0

def is_k() :
    if r-1 < len(data) and c-1 < len(data[0]) :
        if data[r-1][c-1] == k :
            return True
    return False

def update_data() :
    # 개수 세기
    temp_matrix = []
    max_value = 0
    for i in range(len(data)) :
        nums = set(data[i])
        temp = []
        for num in nums :
            if num == 0 : # 값이 0일 경우 무시
                continue
            temp.append((num, data[i].count(num))) # (수, 등장 횟수) 형태로 추가
        max_value = max(max_value, len(temp) * 2)
        temp_matrix.append(temp)

    # 정렬 작업 수행
    for i in range(len(temp_matrix)) :
        temp_matrix[i].sort(key=lambda x: (x[1], x[0])) # 등장횟수 커지는 순 -> 수가 커지는 순

    # 길이 맞추고 배열에 삽입
    for i in range(len(temp_matrix)) :
        value = []
        for j in range(len(temp_matrix[i])) :
            value.append(temp_matrix[i][j][0])
            value.append(temp_matrix[i][j][1])
        # 0으로 채운다
        value.extend([0] * (max_value - len(value)))
        data[i] = value

while time < 101 :
    # k 값이 일치한지 확인
    if is_k() :
        print(time)
        break

    time += 1 # 시간 증가
    if len(data) >= len(data[0]) : # R 연산
        update_data()
    else : # C 연산
        data = list(map(list, zip(*data))) # 행과 열 바꾸기
        update_data()
        data = list(map(list, zip(*data))) # 다시 행과 열 바꾸기

else :
    print(-1)
   
  
'''
1. is_k() 함수를 통해 data[r-1][c-1]의 값이 k인지 확인하고, 일치하면 시간을 출력한후 작업을 종료하고 일치하지 않다면 시간을 1 증가시킨 후 작업을 계속한다.
2. R 연산에 해당될 경우 update_data() 함수를 호출하고, C 연산에 해당될 경우 data리스트의 행과 열을 바꾼 후 update_data() 함수를 호출한다.
3. update_data() 함수에서는 각 행의 수와 해당 수의 개수를 구하여 (수, 등장 횟수) 형태로 temp 리스트에 추가한다.
4. 이후 값 정렬 시 등장횟수가 커지는 순으로 정렬하고, 이것이 여러 개라면 수가 커지는 순으로 정렬을 수행한다.
5. 정렬 수행이 끝나면 extend() 를 통해 수들을 하나의 리스트 형태로 구성하고 나머지 길이를 0으로 채워준다.

'''
