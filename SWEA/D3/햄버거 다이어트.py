from itertools import combinations

t = int(input())

for tc in range(1, t + 1) :
    n, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    max_score = 0
    for i in range(1, n + 1) :
        for value in combinations(data, i) :
            kcal = 0
            score = 0
            for v in range(len(value)) :
                kcal += value[v][1]
                score += value[v][0]
            if kcal > l :
                continue
            if max_score < score :
                max_score = score

    print('#%d %d' % (tc, max_score))
    
'''
1. 각 테스트 케이스마다 n개의 [점수, 칼로리]를 입력받아 data 리스트에 저장한다.
2. 모든 조합을 구하여 각 조합에서의 칼로리의 총합과 점수 총 합을 구한다.
3. 만약 칼로리의 총합이 l보다 크다면 continue하고, l보다 작거나 같고 score가 max_score보다 크다면 max_score를 score 값으로 갱신한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 max_score 값을 출력한다.

'''
