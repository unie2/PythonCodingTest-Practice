# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())
value = (v - b) / (a - b)

if int(value) == value :
    value = int(value)
else :
    value = int(value) + 1

print(value)


'''
1. 달팽이가 올라갔다 다시 미끄러지는 과정에서 실질적으로 올라갈 수 있는 거리(ex. 3미터 올라가고, 1미터 떨어진다면 실질적으로 올라갈 수 있는 거리는 2미터)를 구해 value에 할당한다.
 
2. 만약 value가 나머지가 없는 값이라면 단순히 정수형으로 변환하고, 그렇지 않다면 한 번 더 올라가야 하므로 정수형으로 변환한 값에 1을 더한다.

'''
