def solution(x):
    answer = True
    temp = x
    sum_value = 0
    while temp != 0 :
        sum_value += temp % 10
        temp //= 10
        
    if x % sum_value != 0 :
        answer = False
    
    return answer
  
'''
1. 반복문을 통해 temp의 값이 0이 될때까지 temp값을 10으로 나눈 나머지 값을 sum_value에 누적한다.
2. temp의 값을 10으로 나눈 값으로 갱신한다.
3. 반복문이 끝나면 전달받은 x를 sum_value로 나눠 도출된 나머지 값을 확인하여 그 값이 0이 아니라면 answer를 False로 갱신한다.

'''
