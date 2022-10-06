# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
start, end = 1, max(data)

while start <= end :
    mid = (start + end) // 2
    count = 0
    for lan in data :
        count += lan // mid

    if count >= n :
        start = mid + 1
    else :
        end = mid - 1

print(end)

'''
1. 백준 2805번 나무 자르기 문제와 이분 탐색 문제 유형이다. 랜선의 길이를 증가 혹은 감소시키면서 n개를 만들 수 있는 랜선의 최대 길이를 구한다.

2. 초기 start, end 값은 각각 1과 입력받은 랜선의 최대값으로 설정한 후 start가 end보다 커질 때까지 while문을 통해 아래와 같은 작업을 반복한다.
  - start와 end의 중간 값(mid)을 구하고, 현재 가지고 있는 랜선의 길이를 각각 mid로 나눠 count에 누적한다.
    이는 각 랜선에서 mid 길이를 잘라낼 수 있는 개수를 의미한다.
  - 만약 count 값이 n 이상일 경우 갖게 되는 개수가 많으므로 start 값을 mid + 1로 갱신하여 자르고자 하는 길이를 증가시킨다.
  - 반대로 count 값이 n보다 작을 경우 갖게 되는 개수가 적으므로 end 값을 mid - 1로 갱신하여 자르고자 하는 길이를 감소시킨다.

'''
