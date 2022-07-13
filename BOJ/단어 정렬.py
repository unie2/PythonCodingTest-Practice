n = int(input())
data = []
for _ in range(n) :
    value = input()
    data.append(value)

data = list(set(data))
data = sorted(data, key=lambda x: (len(x), x))

for d in data :
    print(d)
    
'''
1. n개의 단어를 data 리스트에 저장한 뒤 중복을 제거한다.

2. (1) 길이가 짧은 것부터 (2) 길이가 같으면 사전 순으로 data 리스트의 요소들을 정렬한다.

3. 최종적으로 정렬된 data 리스트의 요소를 하나씩 출력한다.

'''
