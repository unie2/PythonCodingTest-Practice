def solution(x, n):
    answer = []
    num = x
    for i in range(n) :
        answer.append(num)
        num += x
    
    return answer
  
'''
1. 전달받은 x를 num에 삽입한다.
2. n번의 수행을 반복하여 answer 리스트에 현재의 num값을 추가하고 num값을 x를 더한 값으로 갱신한다.
3. 반복문 수행이 끝나면 answer 리스트를 반환한다.

'''
