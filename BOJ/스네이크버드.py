n, l = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for i in range(len(fruit)) :
  if l >= fruit[i] :
    l += 1

print(l)


# 1. 반복문을 통해 fruit 리스트에 존재하는 과일의 높이 값을 하나씩 확인한다.
# 2. 조건문을 통해 현재의 스네이크버드의 길이(l)가 현재 확인하고 있는 과일의 높이보다 크거나 같을 경우 먹을 수 있기 때문에 l에 1을 더한다.
# 3. 반복문 수행이 모두 끝나면 스네이크버드의 길이(l)을 출력한다.
