t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    atom = [list(map(int, input().split())) for _ in range(n)]
    # 0.5초 후에 충돌할 수 있으므로 0.5초 단위로 이동
    # 상 하 좌 우
    directions = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

    result = 0

    # 원자 개수가 2개 미만이라면 충돌할 수 없으므로 종료
    while len(atom) >= 2 :
        for i in range(len(atom)) :
            atom[i][0] = atom[i][0] + directions[atom[i][2]][0]
            atom[i][1] = atom[i][1] + directions[atom[i][2]][1]

        location = {}
        # (좌표): [원자 정보]
        for a in atom :
            try :
                location[(a[0], a[1])].append(a)
            except Exception :
                location[(a[0], a[1])] = [a]

        # 원자 리스트 초기화
        atom = []
        for l in location :
            if len(location[l]) >= 2 : # 충돌하면
                for score in location[l] :
                    result += score[3]
            else :
                # 원자가 1개이고 범위 내에 있다면 atom 리스트에 다시 추가
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000 :
                    atom.append(location[l][0])

    print('#%d %d' % (tc, result))
    
    
'''
1. 각 테스트 케이스마다 n개의 원자 정보를 입력받아 atom 리스트에 정의한다.

2. 0.5초 후에 원자가 충돌할 수 있으므로 0.5초 단위로 이동하는 방향을 의미하는 directions 를 정의한다.

3. 원자(atom)의 개수가 2개 미만이 될 때까지 원자들을 이동시키는 작업을 하며, 아래와 같이 작업을 수행한다.
  - 모든 원자들을 정해진 방향으로 0.5초 단위로 이동시킨다.
  - location 딕셔너리를 정의하여 원자들(atom)을 하나씩 확인하고, (좌표): [원자 정보] 형태로 딕셔너리에 추가한다.
  - 원자(atom) 리스트를 초기화하고 location 딕셔너리를 확인해 해당 위치에 존재하는 원자가 2개 이상일 경우 에너지를 result에 누적시킨다.
  - 만약 해당 위치에 존재하는 원자가 1개이고 범위 내에 있다면 atom 리스트에 해당 원자 정보를 다시 추가한다.
  
4. 위와 같은 반복작업 수행이 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
