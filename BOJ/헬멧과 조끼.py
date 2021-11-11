n, m = map(int, input().split())

hat = list(map(int, input().split()))
top = list(map(int, input().split()))

hat = max(hat)
top = max(top)

print(hat + top)


# 1. 헬멧(hat)과 조끼(top)의 각 방어력 정보를 리스트 형태로 구성하여 입력받는다.
# 2. 다시 헬멧과 조끼에 대하여 해당 리스트에서 가장 큰 방어력을 구하여 갱신한다.
# 3. 최종적으로 헬멧의 최대 방어력값과 조끼의 최대 방어력값을 더하여 출력한다.
