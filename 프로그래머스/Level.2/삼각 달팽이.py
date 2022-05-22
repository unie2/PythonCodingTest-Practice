def solution(n) :
    data = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    num = 1

    for i in range(n) :
        for j in range(i, n) :
            if i % 3 == 0 : # 아래로 이동
                x += 1
            elif i % 3 == 1 : # 오른쪽으로 이동
                y += 1
            elif i % 3 == 2 : # 위로 이동
                x -= 1
                y -= 1

            data[x][y] = num
            num += 1

    answer = []
    for i in range(n) :
        for j in range(n) :
            if data[i][j] != 0 :
                answer.append(data[i][j])

    return answer
  
'''
1. 2차원 리스트 data를 생성하고, 각 x, y에 -1과 0을 할당한다. 또한, 값을 1부터 할당해주기 위해 num을 1로 초기화한다.
2. 2중 for문을 통해 i값을 확인하며, 만약 i가 3으로 나누어떨어지면 아래로 이동해야하므로 x를 1 증가시키고 해당 위치에 num을 할당한 뒤 num을 1 증가시킨다.
3. 만약 i를 3으로 나누었을 때의 나머지 값이 1이라면 오른족으로 이동해야하므로 y를 1 증가시키고 해당 위치에 num을 할당한 뒤 num을 1 증가시킨다.
4. 만약 나머지 값이 2라면 위로 이동해야하므로 x와 y를 1씩 감소시키고 해당 위치에 num을 할당한 뒤 num을 1 증가시킨다.
5. data 리스트에 값을 넣는 작업을 마치면 data 리스트에 존재하는 값을 순서대로 확인하여 그 값이 0이 아니라면 answer 리스트에 추가한다.

'''
