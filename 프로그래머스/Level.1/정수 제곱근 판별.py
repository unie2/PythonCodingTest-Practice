import math

def solution(n):
    data = math.sqrt(n)
    if data == int(data) :
        return (data + 1) ** 2
    
    return -1
  
'''
1. math.sqrt()를 활용하여 n의 제곱근을 구해 data에 할당한다.
2. 만약 data의 값이 정수형으로 변환한 값과 같다면 data + 1의 제곱을 리턴하고, 그렇지 않다면 -1을 리턴한다.

'''
