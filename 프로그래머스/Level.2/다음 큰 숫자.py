def solution(n) :
    temp = n + 1
    while True :
        if str(bin(temp)[2:]).count('1') == str(bin(n)[2:]).count('1') :
            return temp
        temp += 1
        
'''
1. n+1을 temp의 가장 초깃값으로 설정한다.
2. 반복문을 수행하며, temp를 2진수로 변환했을 때 1의 개수와 n을 2진수로 변환했을 때 1의 개수가 같다면 temp를 리턴하고, 다를 경우 temp에 1을 증가시킨다.

'''
