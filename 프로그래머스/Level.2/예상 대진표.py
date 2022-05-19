def solution(n, a, b) :
    answer = 0
    while a != b :
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer
  
'''
1. a와 b의 값이 같아질 때까지 아래와 같은 작업을 반복한다.
  - 현재의 a 값에 1을 더하고 2로 나눈 몫을 a에 갱신한다.
  - 현재의 b 값에 1을 더하고 2로 나눈 몫을 b에 갱신한다.
  - answer 값을 1 증가시킨다.

'''
