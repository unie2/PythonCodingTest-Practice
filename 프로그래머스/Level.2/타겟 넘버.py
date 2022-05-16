def solution(numbers, target) :
    tree = [0] # 초기 값
    for i in range(len(numbers)) :
        value = []
        for j in range(len(tree)) :
            value.append(tree[j] - numbers[i]) # 빼기
            value.append(tree[j] + numbers[i]) # 더하기

        tree = value

    answer = tree.count(target)

    return answer
  
'''
1. 이중 for문을 수행하여 tree[j] 에서 numbers[i]를 뺀 값과 더한 값을 value 리스트에 추가한다.
2. 내부 반복문이 끝나면 tree를 value로 갱신한다.
3. 반복문이 모두 끝나면 tree 리스트에 담겨있는 요소 중 target값의 개수를 가져와 반환한다.

'''
