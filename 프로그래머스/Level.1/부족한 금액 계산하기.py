def solution(price, money, count) :
    answer = 0
    for i in range(1, count + 1) :
        answer += price * i

    if answer - money > 0 :
        return answer - money
    else :
        return 0
      
'''
1. 1부터 count + 1 까지를 반복문의 범위로 설정하여, price * i 값을 answer에 누적한다.
2. 만약 answer에서 money를 뺀 값이 0보다 크다면 금액이 부족하므로 answer - money 값을 반환한다.
3. 그렇지 않을 경우 금액이 부족하지 않으므로 0을 반환한다.

'''
