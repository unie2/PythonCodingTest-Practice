from itertools import combinations

def get_sum(candidate) :
    value = 0
    for hx, hy in house :
        temp = 1e9
        for cx, cy in candidate :
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        value += temp

    return value

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n) :
    temp = list(map(int, input().split()))
    for c in range(n) :
        if temp[c] == 1 :
            house.append((r, c)) # 집
        elif temp[c] == 2 :
            chicken.append((r, c)) # 치킨 집

candidates = list(combinations(chicken, m))

result = 1e9
for candidate in candidates :
    result = min(result, get_sum(candidate))

print(result)

'''
1. 도시의 정보를 입력받아 집(1) 과 치킨 집(2)의 위치를 각각 house, chicken 리스트에 추가한다.
2. combinations()를 통해 모든 치킨 집 중에서 m개의 치킨집을 보는 조합을 계산하여 candidates에 할당한다.
3. 조합을 하나씩 꺼내 치킨 거리의 합을 계산하는 함수(get_sum())에서 값을 처리하여 result와 비교하고 더 작은 값으로 갱신한다.
4. get_sum() 함수 내부에서는 모든 집에 대하여 temp = min(temp, abs(hx - cx) + abs(hy - cy)) 코드를 통해 가장 가까운 치킨집의 거리를 찾는다.
5. 이후 가장 가까운 치킨집까지의 거리를 value 변수에 누적하고, 이러한 과정을 모두 마치면 치킨 거리의 합(value)을 반환한다.
6. 최종적으로 치킨 거리의 합의 최소 값을 의미하는 result를 출력한다.

'''
