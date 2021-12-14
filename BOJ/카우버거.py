b, c, d = map(int, input().split())

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

result = 0
min_value = min(b, c, d)
for i in range(min_value) :
  result += (burger[i] + side[i] + drink[i]) * 0.9

result += sum(burger[min_value::])
result += sum(side[min_value::])
result += sum(drink[min_value::])

print(sum(burger) + sum(side) + sum(drink))
print(int(result))


# 1. 각 버거, 사이드 메뉴, 음료의 가격을 입력받아 리스트 형태로 구성하고 세 가지 종류의 음식을 내림차순으로 정렬한다.
# 2. 주문한 버거의 개수(b), 사이드 메뉴의 개수(c), 음료의 개수(d) 중 최소 값을 구해 min_value에 할당한다.
# 3. min_value번째까지 음식들은 할인을 받을 수 있기 때문에 반복문의 범위로 지정하고 내부에서는 해당 인덱스의 각 버거, 사이드 메뉴, 음료의 가격을 더해 0.9를 곱하여 result에 누적한다.
# 4. 반복문이 종료되면 버거, 사이드 메뉴, 음료의 남은 금액의 합을 result에 누적한다.
# 5. 최종적으로 세트 할인이 적용되기 전 가격과 적용된 후의 최소 가격을 출력한다.
