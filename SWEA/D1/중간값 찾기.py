n = int(input())
data = list(map(int, input().split()))

data.sort()
len_value = n // 2
print(data[len_value])

'''
1. n개의 수를 리스트 형태로 구성하고 중간값을 찾기 위해 오름차순으로 정렬한다.
2. n을 2로 나눠 중간 값 인덱스(len_value)를 구한다.
3. 최종적으로 len_value를 인덱스로 가지는 data 리스트 값을 출력한다.

'''
