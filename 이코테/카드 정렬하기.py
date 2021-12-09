import heapq

n = int(input())

heap = []
for i in range(n) :
  data = int(input())
  heapq.heappush(heap, data)

result = 0

while len(heap) != 1 :
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)

  sum_value = a + b
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)


# 1. 이 문제는 우선순위 큐(heapq)를 통해 원소를 넣었다 빼는 것만으로도 정렬된 결과를 얻을 수 있다.
# 2. heap 리스트에 초기 카드 묶음을 모두 삽입한다.
# 3. while문을 통해 heap 리스트의 원소가 1개 남을 때까지 반복 수행한다.
# 4. 반복문 내에서는 가장 작은 2개의 카드 묶음 (a, b)을 꺼내 더한 값을 sum_value에 할당한다.
# 5. sum_value 값을 result에 누적해나가고 다시 heap에 삽입한다.
# * 이 문제의 핵심 아이디어는 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장한다.
