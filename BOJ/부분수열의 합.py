from itertools import combinations

n, s = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(1, n + 1) :
    for value in combinations(data, i) :
        if sum(value) == s :
            result += 1

print(result)

'''
1. combinations() 를 통해 i개의 값들을 도출하고, 도출된 값들의 합이 s와 같다면 result를 1증가시킨다.
2. combinations() 작업을 모두 마치면 최종적으로 result 값을 출력한다.

'''
