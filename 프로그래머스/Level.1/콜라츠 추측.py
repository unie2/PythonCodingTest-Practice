def solution(num):
    count = 0
    while num != 1 :
        if num % 2 == 0 :
            num //= 2
        else :
            num = num * 3 + 1
        count += 1
        
        if count == 500 :
            return -1
        
    return count
  
'''
1. 현재의 num 값이 짝수라면 2로 나눠 값을 갱신한다.
2. 현재의 num 값이 홀수라면 3을 곱하고 1을 더하여 갱신한다.
3. 위 작업을 num 값이 1이 될 때까지 반복하고, 만약 갱신 횟수가 500이 되면 -1을 반환한다.

'''
