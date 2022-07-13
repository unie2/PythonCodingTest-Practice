n = int(input())

data = []
for _ in range(n) :
    x, y = map(int, input().split())
    data.append((x, y))

data = sorted(data, key=lambda x: (x[1], x[0]))

for d in data :
    print(d[0], d[1])
    
'''
1. n개의 (x, y) 좌표를 입력받아 data 리스트에 저장한다.
2. (y 좌표가 증가하는 순) -> (x 좌표가 증가하는 순) 으로 data 리스트 내 요소를 정렬한다.
3. 정렬된 data 리스트의 각 x, y 좌표를 출력한다.

'''
