def solution(n, m):
    answer = []
    # 최대 공약수
    value = min(n, m)
    for i in range(value, 0, -1) :
        if n % i == 0 and m % i == 0 :
            answer.append(i)
            break
    # 최소 공배수
    value = max(n, m)
    for i in range(value, value * value) :
        if i % n == 0 and i % m == 0 :
            answer.append(i)
            break
            
    return answer
  
'''
1. 최대 공약수
   - 전달받은 n과 m의 값 중 작은 값을 value에 할당한다.
   - 반복문을 통해 value부터 1까지 거꾸로 값을 확인하여 그 값을 n과 m에 나눈 나머지 값이 모두 0일 경우 최대공약수이므로 answer 리스트에 추가한 후 반복문을 빠져나온다.
   
2. 최소 공배수
   - 전달받은 n과 m의 값 중 큰 값을 value에 할당한다.
    - 반복문을 통해 value부터 값을 확인하여 그 값에 n과 m을 나눈 나머지 값이 모두 0일 경우 최소 공배수이므로 answer 리스트에 추가한 후 반복문을 빠져나온다.

'''
