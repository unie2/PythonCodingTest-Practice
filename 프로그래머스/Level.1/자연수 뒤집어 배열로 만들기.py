def solution(n):
    answer = []
    while True :
        data = n % 10
        answer.append(data)
        n //= 10
        if n == 0 :
            break
            
    return answer
  
  
'''
1. n을 10으로 나눈 나머지 값을 answer 리스트에 추가한다.
2. n을 10으로 나눈 몫으로 갱신하고, 이와 같은 작업을 반복하여 n의 값이 0일 경우 반복문을 종료한다.
3. 최종적으로 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 answer 리스트를 반환한다.

'''
