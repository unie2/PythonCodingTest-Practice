def solution(left, right) :
    answer = 0
    for i in range(left, right + 1) :
        temp_cnt = 0
        for j in range(1, i + 1) :
            if i % j == 0 :
                temp_cnt += 1

        if temp_cnt % 2 == 0 : # 짝수개라면
            answer += i
        else : # 홀수개라면
            answer -= i

    return answer
  
'''
1. 전달받은 left 값부터 right 값까지 각 약수의 개수를 구한다.
2. 만약 i를 j로 나누었을 때 나누어 떨어진다면 약수이므로 temp_cnt를 1 증가시킨다.
3. 특정 숫자에 대한 약수의 개수를 구한 후, 약수의 개수(temp_cnt)가 짝수라면 answer에 i를 더하고, 홀수라면 i를 뺀다.

'''
