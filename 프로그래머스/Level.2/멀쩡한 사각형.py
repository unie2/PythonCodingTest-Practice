def solution(w, h) :
    gcd = 0
    for i in range(min(w, h), 0, -1) :
        if w % i == 0 and h % i == 0 :
            gcd = i
            break

    answer = w * h - (w + h - gcd)

    return answer
  
# 1. 전달받은 w와 h의 최대 공약수를 구하여 gcd에 할당하고, w * h - (w + h - gcd) 를 계산하여 반환한다.
