# https://www.acmicpc.net/problem/3085

n = int(input())
data = [list(input()) for _ in range(n)]

result = 0

def check_col() :
    global result

    for k in range(n) :
        length = 1
        for l in range(n-1) :
            if data[k][l] == data[k][l+1] :
                length += 1
                result = max(result, length)
            else :
                length = 1

def check_row() :
    global result

    for k in range(n) :
        length = 1
        for l in range(n-1) :
            if data[l][k] == data[l+1][k] :
                length += 1
                result = max(result, length)
            else :
                length = 1

for i in range(n) :
    for j in range(n-1) :
        # 두 원소가 다르다면
        if data[i][j] != data[i][j+1] :
            # swap
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            check_col() # 가로 확인
            check_row() # 세로 확인
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        # 두 원소가 다르다면
        if data[j][i] != data[j+1][i] :
            data[j][i], data[j+1][i] = data[j+1][i], data[j][i]
            check_col()
            check_row()
            data[j][i], data[j + 1][i] = data[j + 1][i], data[j][i]

print(result)


'''
1. n x n 크기의 사탕을 입력받아 2차원 data 리스트에 정의한다.
 
2. 이중 for문을 돌려 가로, 세로 각 상황을 확인하여 만약 두 원소가 다르다면 두 값을 교환해주고 최대값을 구하기 위해 check_col() 함수와 check_row() 함수를 수행한다.
   이후 다른 경우의 수도 확인해봐야 하므로 교환했던 두 값을 다시 원래대로 교환한다.
 
3. check_col() 함수와 check_row() 함수는 각 가로와 세로를 기준으로 연속 부분의 최대값을 구해 result를 갱신해나간다.

'''
