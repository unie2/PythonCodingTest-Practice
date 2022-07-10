n = int(input())
card = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

card.sort()

def binary_search(value, start, end) :
    global card
    if start > end :
        return False
    mid = (start + end) // 2
    if value == card[mid] :
        return True
    elif value < card[mid] :
        return binary_search(value, start, mid - 1)
    else :
        return binary_search(value, mid + 1, end)

for d in data :
    if binary_search(d, 0, len(card) - 1) :
        print(1, end=' ')
    else :
        print(0, end=' ')
        
'''
1. 입력받은 n개의 숫자 카드(card) 리스트를 오름차순으로 정렬한 후 data 리스트의 요소를 하나씩 꺼내 이분 탐색을 수행하여 전달받은 값이 True라면 1을, 아니라면 0을 출력한다.

2. 이분 탐색 binary_search() 함수의 작업은 아래와 같다.
  - 만약 start가 end보다 크다면 역전되어 더 이상 확인할 자료가 없으므로 False를 반환한다.
  - ((start + end) / 2) 값을 계산하여 중간 위치를 구해 mid에 할당한다.
  - 만약 value와 card[mid] 값이 같다면 True를 반환한다.
  - 그렇지 않고 value가 card[mid]보다 작다면 왼쪽 부분에서 확인해야 하므로 매개변수 end를 (mid - 1)로 하여 binary_search() 함수를 재귀호출한다.
  - value가 card[mid]보다 크다면 오른쪽 부분에서 확인해야 하므로 매개변수 start를 (mid + 1)로 하여 binary_search() 함수를 재귀호출한다.

'''
