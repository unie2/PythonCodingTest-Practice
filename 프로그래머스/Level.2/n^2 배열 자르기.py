def solution(n, left, right) :
    answer = []
    for i in range(left, right + 1) :
        answer.append(max(i//n, i%n) + 1)

    return answer
  
'''
1. 전달받은 left부터 right + 1까지를 반복문의 범위로 설정하고, i를 n으로 나눈 몫과 나머지 중 더 큰 값에 1을 더한 값을 answer 리스트에 추가한다.
2. 반복문이 종료되면 최종적으로 answer을 반환한다.

'''
