# https://www.acmicpc.net/problem/2217

n = int(input())

data = []
for _ in range(n) :
    data.append(int(input()))

data.sort()

max_value = 0
for i in range(n) :
    max_value = max(max_value, data[i] * (n - i))

print(max_value)


'''
1. n개의 중량을 입력받아 data 리스트에 할당하고, 오름차순으로 정렬한다.
 
2. 정렬된 중량값을 차례대로 확인하여, 만약 (현재의 중량 * 이후에 남은 중량 개수) 값이 max_value 보다 크다면 그 max_value를 갱신한다.

'''
