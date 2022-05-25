from itertools import combinations

def check(value) :
    flag = True
    for i in range(2, value // 2 + 1) :
        if value % i == 0 :
            flag = False
            break

    return flag

def solution(nums):
    answer = 0
    for value in combinations(nums, 3) :
        if check(sum(value)) : # True라면 소수
            answer += 1

    return answer
  
'''
1. itertools.combinations() 모듈을 통해 nums에 존재하는 3개의 수를 추출하고 추출된 3개의 수의 합을 check() 함수에 전달하여 소수인지 판별한다.
2. check() 함수에서는 for문을 통해 value를 특정 수로 나누었을 때 나누어 떨어진다면 소수가 아니므로 False를 반환하고, value // 2 까지 모두 나누어떨어지지 않는다면 소수이므로 True를 반환한다.
3. check() 함수를 통해 전달받은 값이 True일 경우 answer을 1 증가시킨다. 

'''
