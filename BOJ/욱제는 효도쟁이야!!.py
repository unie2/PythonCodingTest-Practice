n = int(input())

data = list(map(int, input().split()))
data.sort()

print(sum(data[:n-1:]))


# 1. n개의 이동비용을 입력받아 리스트 형태로 구성하여 data에 저장한다.
# 2. 최소한의 이동비용을 구해야하므로 data 리스트를 오름차순으로 정렬한다.
# 3. 정렬된 data 리스트의 첫번째 값부터 n-1번째 값까지의 합을 구하여 출력한다.
