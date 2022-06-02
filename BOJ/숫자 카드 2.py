from bisect import bisect_left, bisect_right

n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
target = list(map(int, input().split()))

def search(data, left_value, right_value) :
    right_index = bisect_right(data, right_value)
    left_index = bisect_left(data, left_value)

    return right_index - left_index

for t in target :
    result = search(data, t, t)
    print(result, end=' ')
    
'''
1. 상근이가 가지고 있는 숫자 카드(data)를 오름차순으로 정렬한다.

2. 각 target 값을 꺼내 search() 함수에 전달하여 상근이가 몇 개 가지고 있는지를 구하여 출력한다.

3. search() 함수의 작업은 아래와 같다.
  - bisect_right() 를 통해 data 리스트에 존재하고 가장 우측에 있는 right_value 값의 인덱스 값을 구하여 right_index에 할당한다.
  - bisect_left() 를 통해 data 리스트에 존재하고 가장 좌측에 있는 left_value 값의 인덱스 값을 구하여 left_index에 할다한다.
  - right_index 값과 left_index 값의 차를 반환한다.

'''
