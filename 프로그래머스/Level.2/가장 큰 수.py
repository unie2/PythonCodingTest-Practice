def solution(numbers) :
    answer = ''
    numbers = list(map(str, numbers))
    numbers = (sorted(numbers, key=lambda x: x * 5, reverse=True))

    for value in numbers :
        answer += str(value)

    return str(int(answer))
  
'''
1. 전달받은 numbers의 요소들을 문자열 형태로 변환해준다.
2. numbers 리스트를 (첫 번째 자리 높은 순) -> (문자열의 길이가 높은 순) 으로 정렬한다.
  ** 참고 : 각 문자에 5를 곱해 해당 문자가 5번 반복되게 한 후 그 문자열을 통해 정렬을 수행
3. 정렬된 numbers 리스트의 문자열을 하나씩 꺼내 answer에 이어 붙인다.
4. 모든 문자열을 이어붙이면, 최종적으로 answer를 반환한다.

'''
