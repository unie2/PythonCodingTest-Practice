n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값 출력
print(data[(n-1) // 2])


# 1. 리스트 형태로 구성하여 값들을 입력 받고, 오름차순으로 정렬을 수행한다.
# 2. 단순히 중간값을 출력함으로써 문제를 해결할 수 있다.
