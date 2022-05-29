from copy import deepcopy

max_diff = 0
answer = []

def dfs(info, shoot, n, i) :
    global answer, max_diff
    if i == 11 :
        if n != 0 :
            shoot[10] = n
        score_diff = calcDiff(info, shoot)
        if score_diff <= 0 :
            return
        result = deepcopy(shoot)
        if score_diff > max_diff :
            max_diff = score_diff
            answer = [result]
            return

        if score_diff == max_diff :
            answer.append(result)
        return

    # 점수 먹는 경우
    if info[i] < n :
        shoot.append(info[i] + 1)
        dfs(info, shoot, n-info[i]-1, i + 1)
        shoot.pop()

    # 점수 안먹는 경우
    shoot.append(0)
    dfs(info, shoot, n, i + 1)
    shoot.pop()

def calcDiff(info, shoot) :
    enemyScore, myScore = 0, 0
    for i in range(11) :
        if (info[i], shoot[i]) == (0, 0) :
            continue
        if info[i] >= shoot[i] :
            enemyScore += (10 - i)
        else :
            myScore += (10 - i)

    return myScore - enemyScore


def solution(n, info) :
    global answer, max_diff
    dfs(info, [], n, 0)
    if answer == [] :
        return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]
  
'''
1. dfs() 함수를 통해 가장 큰 점수 차이로 우승하기 위한 리스트를 받고, 만약 리스트가 비어 있을 경우 [-1]을 반환하고,
   그렇지 않다면 가장 낮은 점수를 맞힌 개수가 더 많은 순으로 정렬하여 첫 번째 리스트를 반환한다.

2. dfs() 함수의 작업은 아래와 같다.
  - 어피치가 맞힌 과녁의 각 개수를 하나씩 확인하여 그 값이 n보다 작을 경우
    라이언이 각 과녁을 맞힌 개수를 의미하는 shoot에 info[i] + 1을 추가하고, 재귀 호출을 수행한 뒤 값을 빼준다(pop).
  - 점수를 먹지 않는 경우에는 shoot에 0을 추가하고 dfs() 함수를 재귀호출한 뒤 값을 빼준다.
  - 이와 같은 방식으로 계속해서 재귀호출을 수행하다가 i가 11이 되었을 때 info와 shoot을 통해 점수의 차이를 구한다.
  - 만약 점수의 차이가 0보다 작거나 같다면 return한다.
  - shoot 리스트를 result에 복사하고, 만약 현재의 점수 차이가 max_diff 보다 클 경우 max_diff를 현재 차이로 갱신하고 answer에 [result]를 담아 return한다.
  - 만약 현재의 점수 차이와 max_diff 값이 같을 경우 answer 리스트에 result 리스트를 추가하고 return한다.

3. 점수 차이를 구하는 calcDiff() 함수의 작업은 아래와 같다.
  - 어피치가 획득한 점수(enemyScore), 라이언이 획득한 점수(myScore)를 0으로 초기화한다.
  - 0부터 10까지 확인하며, info[i](어피치)와 shoot[i](라이언) 이 모두 0일 경우 둘 다 점수를 획득할 수 없으므로 continue한다.
  - 만약 특정 과녁에 대하여 어피치가 라이언보다 맞힌 개수가 많다면 enemyScore에 (10 - i)를 누적한다.
  - 만약 라이언이 맞힌 개수가 많다면 myScore에 (10 - i)를 누적한다.
  - myScore - enemyScore 의 값을 반환한다.

'''
