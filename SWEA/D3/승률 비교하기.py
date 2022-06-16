t = int(input())

result = []
for tc in range(1, t + 1) :
    a, b, c, d = map(int, input().split())
    alice = a / b
    bob = c / d

    if alice == bob :
        result.append('DRAW')
    elif alice > bob :
        result.append('ALICE')
    else :
        result.append('BOB')

for idx, value in enumerate(result) :
    print('#%d %s' % (idx + 1, value))
    
'''
1. 각 테스트 케이스마다 a, b, c, d를 입력받고, a / b 값을 alice에 할당하고 c / d 값을 bob에 할당한다.
2. alice 값과 bob 값이 같을 경우 'DRAW'를, alice가 더 클 경우 'ALICE'를, bob이 더 클 경우 'BOB'을 result 리스트에 추가한다.
3. 모든 테스트 케이스에 대한 작업 처리를 마치면 최종적으로 enumerate() 를 통해 테스트 케이스 번호와 result에 담긴 요소를 출력한다.

'''
