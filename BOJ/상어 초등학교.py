from heapq import heappush, heappop

# 만족도 0이면 0, 1이면 1, 2면 10, 3이면 100, 4면 1000
def satisfied() :
    result = 0
    for r in range(n) :
        for c in range(n) :
            if not board[r][c] :
                continue
            cnt = 0
            for d in range(4) :
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < n and 0 <= nc < n) :
                    continue
                if board[nr][nc] in likeinfo[board[r][c]] : # 좋아하는 학생 인접한 칸에 있으면
                    cnt += 1
            if cnt : # 10의 -1승이 더해지는 것을 방지
                result += 10 ** (cnt - 1)
    return result

def drawIdx(idx) :
    priorityQueue = [] # 최대 힙 사용 (우선순위 큐로 활용)
    for r in range(n) :
        for c in range(n) :
            if board[r][c] :
                continue
            likeCnt, blankCnt = 0, 0
            for d in range(4) :
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < n and 0 <= nc < n) :
                    continue
                if board[nr][nc] in likeinfo[idx] : # 좋아하는 학생 Set에 있으면
                    likeCnt += 1
                if not board[nr][nc] : # 빈 공간이면
                    blankCnt += 1
            # 최대 힙에 삽입 (우선순위)
            heappush(priorityQueue, (-likeCnt, -blankCnt, r, c))
    like, blank, r, c = heappop(priorityQueue) # 가장 높은 우선순위의 값 뽑은 정보
    board[r][c] = idx

n = int(input())
board = [[0] * n for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

likeinfo = dict() # {학생 번호 : 좋아하는 학생 Set}
for _ in range(n ** 2) :
    info = list(map(int, input().split()))
    likeinfo[info[0]] = set(info[1:])

# 주어진 순서대로 학생 자리 배치
for idx in likeinfo.keys() :
    drawIdx(idx)

# 만족도 조사 결과 출력
print(satisfied())


'''
1. likeinfo 딕셔너리를 통해 {학생번호 : 좋아하는 학생 Set}을 할당하고, 주어진 순서대로 학생 자리를 배치하기 위해 drawIdx 함수를 호출한다.
2. drawIdx 함수 내부에서는 우선순위 큐로 활용할 수 있도록 최대 힙을 사용한다.
3. 정의한 방향에 있는 칸을 하나씩 확인하여 그 칸이 자리에 앉을 학생(idx)이 좋아하는 학생 Set에 존재하면 likeCnt를 1 증가시키고, 만약 그 칸이 빈 공간이라면 blankCnt를 1 증가시킨다.
4. 방향을 모두 확인하면 문제에서 제시한 우선순위에 맞게 최대 heap에 넣어준다. 기본적으로 최소 힙이므로 취대 힙으로 들어갈 수 있도록 음수 부호(-)를 붙여준다.
5. 가장 높은 우선순위의 값을 뽑아 자리를 배치시켜준다.
6. 자리 배치가 모두 끝나면 만족도 조사를 위해 satisfied() 함수를 호출한다.
7. satisfied() 함수 내부에서는 특정 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구하고, 그 값에 따라 문제에서 제시한 만족도를 result에 누적한다.
8. 여기서 만약 좋아하는 학생의 수가 0일 경우 -1 이므로 10의 -1승이 누적될 수 없도록 조건문을 포함시켜준다.
9. 최종적으로 만족도 조사 결과를 출력한다.

'''
