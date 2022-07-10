import sys

input = sys.stdin.readline
n = int(input())
data = [0] * 10001

for _ in range(n) :
    data[int(input())] += 1

for i in range(10001) :
    if data[i] != 0 :
        for j in range(data[i]) :
            print(i)
            
'''
1. sys.stdin.readline 을 input에 할당하여 값을 입력받을 때 사용하도록 한다.
2. n개의 값을 입력받는데, 하나의 값을 입력받을 때마다 그 값을 인덱스로 하여 data 값을 1 증가시킨다.
3. data 리스트의 요소를 하나씩 확인하여 그 값이 0이 아닐 경우 그 값을 개수로 하여 해당 인덱스 번호를 j번 출력한다.

'''
