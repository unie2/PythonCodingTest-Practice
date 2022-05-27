def solution(n) :
    for i in range(2, n) :
        if n % i == 1 :
            return i
          
# 1. 2부터 n까지를 반복문의 범위로 설정하고, n을 i로 나누었을 때 나머지 값이 1일 경우 i를 반환한다.
