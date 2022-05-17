def solution(n):
    answer = [0, 1, 1]
    for i in range(3, n + 1) :
        answer.append(answer[i-1] + answer[i-2])
    
    
    return (answer[n]) % 1234567
  
'''
1. answer 리스트의 3번째 요소부터 n까지 각 위치의 피보나치 수를 구성한다.
2. 반복문이 종료되면 최종적으로 answer[n] 의 값을 1234567로 나눈 나머지를 반환한다.

'''
