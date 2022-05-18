def rotate(data, start_x, start_y, end_x, end_y) :
    info = [data[start_x-1][start_y-1]]
    # start_x 열
    for i in range(start_y, end_y) :
        info.append(data[start_x-1][i])
        data[start_x-1][i] = info[-2]
    # end_y 행
    for i in range(start_x, end_x) :
        info.append(data[i][end_y-1])
        data[i][end_y-1] = info[-2]
    # end_x 열
    for i in range(end_y-2, start_y-2, -1) :
        info.append(data[end_x-1][i])
        data[end_x-1][i] = info[-2]
    # start_y 행
    for i in range(end_x-2, start_x-2, -1) :
        info.append(data[i][start_y-1])
        data[i][start_y-1] = info[-2]

    return data, min(info)

def solution(rows, columns, queries) :
    answer = []

    data = [[0] * columns for _ in range(rows)]
    index = 1
    for i in range(rows) :
        for j in range(columns) :
            data[i][j] = index
            index += 1

    for start_x, start_y, end_x, end_y in queries :
        data, min_value = rotate(data, start_x, start_y, end_x, end_y)
        answer.append(min_value)

    return answer
  
  
'''
1. rows * columns 크기의 2차원 data 리스트를 정의하고, 각 칸에 index를 1씩 증가시키면서 값을 삽입한다.

2. queries의 요소를 가져와 data 리스트와 함께 rotate() 함수의 매개변수로 전달하여 테두리를 회전하고 최솟값을 반환받는다.

3. 행렬 테두리를 회전시키는 rotate() 함수의 작업은 아래와 같다.
  - 첫번째 좌표(start_x, start_y)를 기준으로 (동 남 서 북) 순서로 값을 확인한다.
  - 확인하는 값을 info 리스트에 추가하고, 갱신된 info 리스트에서 뒤에서 두 번째에 존재하는 값이 이전 값이므로 현재 확인하는 값을 뒤에서 두 번째 값으로 갱신한다.
  - 갱신된 data 리스트와 info 리스트에 존재하는 최솟값을 반환한다.

4. min_value 값을 answer 리스트에 추가하고, 위와 같은 반복 작업을 모두 마치면 최종적으로 answer 리스트를 반환한다.

'''
