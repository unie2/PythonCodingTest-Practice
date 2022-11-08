# https://www.acmicpc.net/problem/2309

def combinations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in combinations(arr[i+1:], r-1) :
                yield [arr[i]] + next

data = [int(input()) for _ in range(9)]

result = []
for value in combinations(data, 7) :
    if sum(value) == 100 :
        result = sorted(value)
        break

for res in result :
    print(res)
    
    
'''
1. 입력된 9개의 값들을 data 리스트에 정의하고, 조합(combinations)을 통해 data 리스트에서 7개의 수를 도출해낸다.
 
2. 만약 도출해낸 7개의 수의 합이 100일 경우 오름차순으로 정렬하여 result에 할당하고 break 한다.
 
3. 최종적으로 result 리스트에 존재하는 값들을 하나씩 출력한다.

'''
