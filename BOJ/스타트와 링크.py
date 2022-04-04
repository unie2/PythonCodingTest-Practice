def cal_diff(team1, team2) :
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)) :
        for j in range(len(team1)) :
            sum_team1 += board[team1[i]][team1[j]]
            sum_team2 += board[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)


def make_team(team1, count, n, start) :
    global result

    if count == n // 2 :
        team2 = []
        for i in range(n) :
            if i not in team1 :
                team2.append(i)

        diff = cal_diff(team1, team2)
        result = min(result, diff)
        return

    for i in range(start, n) :
        if i not in team1 :
            team1.append(i)
            make_team(team1, count + 1, n, i + 1)
            team1.remove(i)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = int(1e9)
make_team([], 0, n, 0)

print(result)

'''
1. 팀을 구성하는 make_team 함수와 두 팀의 능력치 차이를 반환해주는 cal_diff 함수로 문제를 해결할 수 있다.
2. make_team 함수 내에서는 전달받은 count값이 n // 2 의 값과 같은지 확인한다.
3. 같다면 team2에 team1에 없는 인덱스 i 값을 추가한다. 이후 cal_diff 함수를 통해 두 팀의 능력치 차이를 절대값으로 받고, 현재의 result 값과 비교하여 더 작은 값으로 result 값을 갱신하여 반환한다.
4. count값과 n // 2 값이 같지 않을 경우 재귀호출을 통해 값이 같아질때까지 반복 수행해준다.

'''
