n = int(input())
data = []
for _ in range(n) :
    data.append(int(input()))

data.sort()

for value in data :
    print(value)
    
'''
1. n개의 수를 입력받아 data 리스트에 저장한다.
2. data 리스트에 존재하는 값들을 오름차순으로 정렬한다.
3. data 리스트의 요소를 하나씩 꺼내 출력한다.

'''
