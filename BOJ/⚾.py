# https://www.acmicpc.net/problem/17281

def dfs(count) :
    global result
    if count == 9 :
        start, score = 0, 0
        for inning in data :
            b1, b2, b3, out = 0, 0, 0, 0
            while out < 3 :
                pos = select[start]
                if inning[pos] == 0 : # 아웃
                    out += 1
                elif inning[pos] == 1 : # 안타
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[pos] == 2 : # 2루타
                    score += b3 + b2
                    b1, b2, b3 = 0, 1, b1
                elif inning[pos] == 3 : # 3루타
                    score += b3 + b2 + b1
                    b1, b2, b3 = 0, 0, 1
                else : # 홈런
                    score += b3 + b2 + b1 + 1
                    b1, b2, b3 = 0, 0, 0

                start = (start + 1) % 9
        result = max(result, score)
        return

    for i in range(9) :
        if check[i] == 1 :
            continue
        check[i] = 1
        select[i] = count
        dfs(count + 1)
        check[i] = 0
        select[i] = 0

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
select = [0 for _ in range(9)] # 타순
check = [0 for _ in range(9)] # 중복 검사 리스트
check[3] = 1

result = 0
dfs(1)
print(result)

'''
1. 타순 정보를 담을 select 리스트, 방문 여부를 확인할 수 있는 중복 검사 check 리스트를 정의하고, 1번 타자는 4번째로 정해졌으므로 check[3](0번째 인덱스부터 시작하므로)를 1로 갱신한다.

2. dfs() 함수를 통해 최대 점수(result)를 구하여 출력한다. dfs() 함수의 작업은 아래와 같다.
  - 0번째 인덱스부터 8번째 인덱스까지 순서대로 check[i] 값을 확인한다.
  - check[i] 값이 이미 1일 경우 continue한다.
  - check[i] 값이 0이라면 1로 갱신하고 select[i]에 타순(count)을 할당하고 dfs() 함수를 재귀호출한다. 이후 check[i]와 select[i]의 값은 다시 0으로 되돌린다.
 
  - count 값이 9라면 타순이 모두 정해졌으므로  start(선수)와 score(점수)를 0으로 초기화하고, 이닝 정보를 하나씩 확인하여 아래와 같이 작업한다.
    - select[start]를 구하고, 만약 inning[pos]가 0일 경우(아웃) out 값을 1 증가시킨다.
    - inning[pos]가 1일 경우(안타) 한 루씩 진루하므로 3루(b3) 값을 score에 누적하고 b1, b2, b3에 선수를 재배치시켜줌으로써 값을 갱신한다.
    - inning[pos]가 2일 경우(2루타) 두 루씩 진루하므로 3루(b3)와 2루(b2) 값을 score에 누적하고 b1, b2, b3에 선수를 재배치시켜줌으로써 값을 갱신한다.
    - inning[pos]가 3일 경우(3루타) 세 루씩 진루하므로 3루(b3)와 2루(b2)와 1루(b1) 값을 score에 누적하고 b1, b2, b3 값을 갱신한다.
    - inning[pos]가 4일 경우(홈런) 모든 주자가 홈까지 진루하므로 3루(b3)와 2루(b2)와 1루(b1)와 현재의 선수(1) 값을 score에 누적하고 b1, b2, b3 값을 모두 0으로 초기화한다.
    - 이후 다음 타석을 start에 할당한다.
    - 이와 같은 작업을 out 값이 3이 될 때까지 반복 수행한다.
  - 이닝이 끝나면 최대 점수를 result에 할당하고 return 한다.

'''
