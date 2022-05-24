def solution(n) :
    answer = 0

    while n > 0 :
        if n % 2 == 1 :
            answer += 1
        n //= 2
    
    return answer
  
  
'''
1. n이 0 이하가 될 때까지 반복 수행하는데, 현재 n 값을 2로 나눈 나머지가 1일 경우 한 칸 점프해야하므로 answer을 1 증가시킨다.
2. n을 2로 나눈 몫으로 갱신한다.
3. 반복문이 종료되면 최종적으로 answer 값을 반환한다.

'''
