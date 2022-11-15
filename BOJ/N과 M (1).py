# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())

def permutations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in permutations(arr[:i] + arr[i+1:], r-1) :
                yield [arr[i]] + next

data = [i for i in range(1, n + 1)]
for value in permutations(data, m) :
    print(* value)
    
    
'''
1. n과 m을 입력받아 1부터 n까지의 수를 data 리스트에 정의한다.
 
2. 순열(permutations)을 통해 각 경우의 수마다 m개의 수를 도출해내 해당 수들을 출력한다.

'''
