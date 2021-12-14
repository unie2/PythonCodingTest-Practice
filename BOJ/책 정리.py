n, m = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

for i in range(len(book)) :
  for j in range(len(box)) :
    if book[i] > box[j] :
      continue
    box[j] -= book[i]
    break

print(sum(box))


# 1. 박스의 개수와 책의 개수를 각 리스트 형태로 구성하여 저장한다.
# 2. 이중 for문을 통해 현재 확인하고 있는 책의 용량이 현재 확인하고 있는 박스의 용량보다 클 경우 다음 박스를 확인한다.
# 3. 크지 않을 경우 현재의 박스의 값을 현재 책의 용량을 뺀 값으로 갱신한 뒤 내부 반복문을 종료하여 다음 책 용량을 확인한다.
# 4. 반복 수행이 모두 끝나면 box 리스트의 모든 값들의 합을 출력한다.
