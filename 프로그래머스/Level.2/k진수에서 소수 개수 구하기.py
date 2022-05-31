from math import sqrt

def check(data) :
    if data <= 1 :
        return False
    for i in range(2, int(sqrt(data)) + 1) :
        if data % i == 0 :
            return False
    return True

def solution(n, k) :
    answer = 0
    value = ''
    while n > 0 :
        a, b = divmod(n, k)
        n //= k
        value += str(b)

    value = value[::-1]
    for i in value.split('0') :
        if i.isdigit() and check(int(i)) :
            answer += 1

    return answer
  
'''
1. 전달받은 n을 k진수로 변환하여 value에 정의하고, '0'으로 나눠 각 값을 확인하는데 그 값이 숫자이고 소수라면 answer을 1 증가시킨다.

2. 소수 판별 check() 함수의 작업은 아래와 같다.
  - 전달받은 data 값이 1 이하라면 False를 반환한다.
  - 2부터 data 값의 제곱근+1 까지를 반복문의 범위로 설정하여 data를 i로 나누었을 때 나누어 떨어진다면 소수가 아니므로 False를 반환한다.
  - 반복문이 끝날때까지도 False가 반환되지 않았다면 True를 반환한다.

'''
