from itertools import permutations
import math

def is_prime(x) :
    for i in range(2, int(math.sqrt(x) + 1)) :
        if x % i == 0 :
            return False
    return True

def solution(numbers) :
    answer = 0
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1) :
        checked = []
        for value in permutations(numbers, i) :
            temp = ''
            if int(value[0]) == 0 :
                continue
            for j in range(len(value)) :
                temp += value[j]
            if int(temp) == 1 :
                continue

            if int(temp) not in checked :
                if is_prime(int(temp)) :
                    answer += 1
                    checked.append(int(temp))
    return answer
  
'''
1. 전달받은 numbers 문자열을 리스트 형태로 변환한다.

2. 순열(permutations)을 통해 조합된 문자열을 가져온 후 아래와 같은 작업을 수행한다.
  - 만약 조합된 value의 0번째 요소가 0일 경우 소수를 판별할 수 없으므로 continue 한다.
  - temp 문자열에 조합된 문자열을 추가한다.
  - 만약 temp 문자열을 정수형으로 변환한 값이 1일 경우 1은 소수에 해당하지 않으므로 continue 한다.
  - 1이 아닌 수이고, checked 리스트에 존재하지 않는 값이라면 is_prime() 함수를 통해 소수를 판별한다.
  - 소수가 맞다면 answer 값을 1 증가시킨 후 정수형으로 변환한 temp 값을 checked 리스트에 추가한다.

3. 소수 판별을 위한 is_prime() 함수의 작업은 아래와 같다.
  - 반복문의 범위는 (2 ~ 전달받은 x의 제곱근 +1) 로 설정한다.
  - x를 i로 나누어 떨어진다면 소수가 아니므로 False를 반환하고, 반복문이 끝날때까지도 False가 반환되지 않았다면 소수이므로 True를 반환한다.

'''
