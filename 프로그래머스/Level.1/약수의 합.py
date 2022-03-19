def solution(n):
    data = []
    for i in range(n//2, 0, -1) :
        if n % i == 0 :
            data.append(i)
    data.append(n)
    
    result = sum(data)
    return result
  
'''
1. 반복문을 통해 n의 절반부터 0까지 하나씩 값을 감소시키면서 확인한다.
2. n을 현재 확인하고 있는 값으로 나눈 나머지 값이 0이라면 n의 약수이므로, data리스트에 추가한다.
3. 전달받은 n의 값 또한 약수에 해당되므로 data리스트에 추가한다.
4. 최종적으로 data리스트에 존재하는 요소들의 합을 도출하여 반환한다.

'''
