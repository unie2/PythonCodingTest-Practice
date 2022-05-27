def solution(sizes) :
    max_weight, max_height = 0, 0
    for a, b in sizes :
        if a < b :
            a, b = b, a
        if max_weight < a :
            max_weight = a
        if max_height < b :
            max_height = b

    return max_height * max_weight
  
'''
1. sizes 리스트에 존재하는 요소를 하나씩 확인하며, 가로의 길이(a)가 세로의 길이(b) 보다 더 크도록 갱신한다.
2. 만약 가로의 길이가 max_weight보다 크다면 max_weight을 a로 갱신한다.
3. 만약 세로의 길이가 max_height보다 크다면 max_height을 b로 갱신한다.
4. 최종적으로 가로의 최대 길이(max_weight)와 세로의 최대 길이(max_height)를 곱한 값을 반환한다.

'''
