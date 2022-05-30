def solution(dirs) :
    x, y = 0, 0
    nx, ny = 0, 0
    visited = []
    answer = 0

    for dir in dirs :
        if dir == 'U' : # 위로 한 칸 이동
            ny += 1
        elif dir == 'D' : # 아래로 한 칸 이동
            ny -= 1
        elif dir == 'L' : # 왼쪽으로 한 칸 이동
            nx -= 1
        elif dir == 'R' : # 오른쪽으로 한 칸 이동
            nx += 1

        if abs(nx) > 5 or abs(ny) > 5 :
            nx, ny = x, y
            continue

        if (x, y, nx, ny) not in visited :
            visited.append((x, y, nx, ny))
            visited.append((nx, ny, x, y))
            answer += 1

        x, y = nx, ny

    return answer
  
'''
1. 현재 좌표(x, y)와 이동할 좌표(nx, ny)를 모두 0으로 초기화하고 방문처리를 위한 visited 리스트와 결과를 담을 answer을 초기화한다.
2. 전달받은 dirs의 문자를 하나씩 확인하며(dir), 만약 dir이 'U'일 경우 ny를 1 증가시킴으로써 위로 한 칸 이동한 좌표를 담는다.
3. 만약 dir이 'D'일 경우 ny를 1 감소시킴으로써 아래로 한 칸 이동한 좌표를 담는다.
4. 만약 dir이 'L'일 경우 nx를 1 감소시킴으로써 왼쪽으로 한 칸 이동한 좌표를 담는다.
5. 만약 dir이 'R'일 경우 nx를 1 증가시킴으로써 오른족으로 한 칸 이동한 좌표를 담는다.
6. nx의 절대값이 5보다 크거나 ny의 절대값이 5보다 클 경우 좌표의 범위에서 넘어가므로 nx, ny를 다시 x, y로 갱신시켜준 뒤 continue한다.
7. continue 되지 않았을 경우 (x, y, nx, ny)가 visited에 존재하는지 확인하고, 없다면 (x, y, nx, ny)와 (nx, ny, x, y)를 visited에 추가한 뒤 answer을 1 증가시킨다.
8. 이후 x와 y를 nx, ny로 갱신시켜 이동처리한다.
9. dirs의 모든 요청을 수행하면 최종적으로 answer을 반환한다.

'''
