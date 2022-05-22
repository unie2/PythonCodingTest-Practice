def solution(number, k) :
    stack = [number[0]]
    for num in number[1:] :
        # stack과 k가 0보다 크고, stack의 마지막 요소가 num보다 작을 경우 반복
        while len(stack) > 0 and k > 0 and stack[-1] < num :
            k -= 1
            stack.pop()
        stack.append(num)

    if k > 0 :
        stack = stack[:-k]

    return ''.join(stack)
  
'''
1. number 문자열의 첫번째 문자를 stack 리스트에 할당한다.
2. 반복문으로 통해 number 문자열의 두 번째 문자를 하나씩 확인하며, stack과 k가 0보다 크고 stack의 마지막 요소가 현재 확인하고 있는 수보다 작을 경우 k를 1 감소시키고 stack의 마지막 요소를 제거하는 작업을 반복한다.
3. while문을 빠져나오면 stack에 현재 num 값을 추가한다.
4. 모든 문자를 확인하여 처리하는 작업을 마쳤으면 k값을 확인하고, k가 0보다 크다면 stack[:-k]를 stack에 할당한다.
5. 최종적으로 stack의 요소를 이어붙인 문자열을 반환한다.

'''
