n = int(input())
data = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
data.sort()

def binary_search(data, t, start, end) :
    if start > end :
        return 0
    mid = (start + end) // 2
    if t == data[mid] :
        return 1
    elif t > data[mid] :
        return binary_search(data, t, mid + 1, end)
    else :
        return binary_search(data, t, start, mid - 1)

for t in target :
    print(binary_search(data, t, 0, n - 1))
    

'''
1. 이분 탐색을 통해 시간 초과 판정없이 문제를 해결할 수 있다.

2. 입력받은 각 target 값이 data 리스트에 존재하는지 이분 탐색을 통해 확인하기 위해 data 리스트를 오름차순으로 정렬한다.

3. data 리스트와 각 target 값(t), 수를 찾기 위한 data 리스트 확인 범위(0~ n-1)를 binary_search() 함수에 전달하여 수행하고, 반환받은 값을 출력한다.

4. binary_search() 함수의 작업은 아래와 같다.
  - start 값이 end 값을 역전하면 찾고자 하는 값이 data 리스트에 존재하지 않으므로 0을 반환한다.
  - (start + end) // 2 를 수행하여 중간 인덱스 값을 도출하여 mid에 할당한다.
  - 만약 찾고자 하는 t 값과 data[mid] 값이 같다면 1을 반환한다.
  - 만약 t가 data[mid]보다 더 크다면 mid 인덱스의 좌측에 존재하는 값들은 더 이상 확인해 볼 필요가 없으므로 start 값을 mid + 1로 설정하여 함수를 재귀 호출한다.
  - 만약 t가 data[mid]보다 작다면 mid 인덱스의 우측에 존재하는 값들은 더 이상 확인해 볼 필요가 없으므로 end 값을 mid - 1로 설정하여 함수를 재귀 호출한다.

'''
