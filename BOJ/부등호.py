# https://www.acmicpc.net/problem/2529

### Case 1 ###
# PyPy3 성공
def permutations(arr, r) :
    for i in range(len(arr)) :
        if r == 1 :
            yield [arr[i]]
        else :
            for next in permutations(arr[:i] + arr[i+1:], r - 1) :
                yield [arr[i]] + next

k = int(input())
data = list(input().split())
max_value = '0'
min_value = '987654321'

for value in permutations([n for n in range(0, 10)], k + 1) :
    flag = 0
    for i in range(k) :
        if data[i] == '<' :
            if value[i] > value[i+1] :
                flag = 1
                break
        elif data[i] == '>' :
            if value[i] < value[i+1] :
                flag = 1
                break

    if flag == 1 :
        continue
    value = ''.join(map(str, value))
    max_value = max(max_value, value)
    min_value = min(min_value, value)

print(max_value)
print(min_value)

'''
1. permutations() 를 통해 k + 1개의 수를 뽑아내 부등호 식이 옳은지 확인하는 방식이다.
   itertools 라이브러리에 존재하는 permutations()를 사용할 수도 있지만, 직접 permutations() 함수를 구현해보았다.
 
2. k + 1개의 수를 도출하고(value), 부등호(data)를 하나씩 확인한다.
 
3. data[i]가 '<'일 경우 value[i]가 value[i+1]보다 작아야 하므로, 만약 value[i]가 value[i+1]보다 크다면 flag를 1로 갱신하고 break한다.
 
4. data[i]가 '>'일 경우 value[i]가 value[i+1]보다 커야 하므로, 작다면 flag를 1로 갱신하고 break한다.
 
5. flag 값이 1일 경우 올바른 부등호 식이 아니므로 continue한다.
 
6. 올바른 부등호 식이라면 value에 존재하는 요소들을 문자열 형태로 이어붙여 max_value보다 크다면 max_value를 갱신하고, min_value보다 작다면 min_value를 갱신한다.

'''


### Case 2 ###
# Python3 성공
k = int(input())
data = list(input().split())

result = []
flag = [False] * 10

def func(index, num) :
    if index == k + 1 :
        result.append(num)
        return

    for i in range(10) :
        if flag[i] == True :
            continue

        if index == 0 or check(num[index-1], str(i), data[index-1]) :
            flag[i] = True
            func(index + 1, num + str(i))
            flag[i] = False

def check(prev, next, oper) :
    if oper == '<' :
        if prev > next :
            return False
    if oper == '>' :
        if prev < next :
            return False

    return True

func(0, '')

result.sort()
print(result[-1])
print(result[0])

'''
1. 재귀 호출을 통해 수를 하나씩 이어붙여 올바른 부등호 식을 result 리스트에 추가하는 방식이다.
 
2. 0부터 9까지의 각 수의 사용 여부를 담은 flag 리스트를 정의하고, func() 함수를 호출한 후 정의된 result 리스트를 오름차순으로 정렬하여 마지막 요소(최댓값)과 첫 번째 요소(최솟값)을 출력한다.
 
3. func() 함수의 작업은 아래와 같다.
  - 만약 index가 k + 1일 경우 수를 뽑아내야 할 갯수만큼 다 뽑았으므로 result 리스트에 num 을 추가하고 return한다.
 
  - 0부터 9까지의 수를 대상으로 사용 여부를 확인하여, 해당 수를 이미 사용했으면 continue한다.
  - 아직 사용하지 않았고, index가 0이거나 (현재까지 정의된 num의 마지막 값, 현재의 값, 부등호)를 매개변수로 하여 check() 함수를 호출하여 반환받은 값이 True라면 해당 수의 사용 여부를 True로 갱신하고 func() 함수를 재귀 호출한다.
  - func() 함수를 재귀 호출한 후에는 다른 값들도 확인해야 하므로 해당 수의 사용 여부를 다시 False로 갱신한다.
'''
