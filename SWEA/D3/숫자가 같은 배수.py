from itertools import permutations

t = int(input())

for tc in range(1, t + 1) :
    data = list(map(int, input()))

    result = 'impossible'
    for value in permutations(data, len(data)) :
        if int(''.join(map(str, value))) > int(''.join(map(str, data))) :
            if int(''.join(map(str, value))) % int(''.join(map(str, data))) == 0 :
                result = 'possible'
                break

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 정수를 한 자리씩 나눠 data 리스트에 저장한다.
2. 최종적으로 출력할 result 값을 'impossible'로 초기화한다.
3. 순열(permutations)을 통해 값(value)을 뽑아내고, 그 값이 입력받은 정수보다 크고 배수라면 result를 'possible'로 갱신하고 break한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
