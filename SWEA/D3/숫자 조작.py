from itertools import combinations

t = int(input())

for tc in range(1, t + 1) :
    data = list(map(str, input()))
    target = [i for i in range(len(data))]

    min_value, max_value = int(''.join(data)), int(''.join(data))

    for value in combinations(target, 2) :
        i, j = value
        data[i], data[j] = data[j], data[i]
        if data[0] == '0' :
            data[i], data[j] = data[j], data[i]
            continue
        if int(''.join(data)) < min_value :
            min_value = int(''.join(data))
        if int(''.join(data)) > max_value :
            max_value = int(''.join(data))
        data[i], data[j] = data[j], data[i]

    print('#%d %d %d' % (tc, min_value, max_value))
    
'''
1. 각 테스트 케이스마다 data 문자열을 리스트 형태로 구성하고, 두 문자를 바꿀 인덱스를 추출하기 위한 target 리스트를 정의한다.
2. 문제에서 요구하는 min_value와 max_value를 현재의 data 값을 정수형으로 변환하여 초기화한다.
3. itertools.combinations() 모듈을 통해 각 인덱스에서 2개를 뽑아 두 문자를 바꾼다.
4. 만약 data리스트의 0번째 요소가 '0'이라면 바꾼 값을 원 상태로 복구하고 continue한다.
5. 그렇지 않고, 만약 정수형 data 값이 min_value보다 작을 경우 해당 값을 min_value에 갱신시키고, 최대 값 또한 마찬가지로 수행한다.
6. 다음 확인 작업을 위해 바꾼 값을 원 상태로 복구한다.
7. 조합을 활용한 반복 작업이 모두 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 최솟값(min_value)와 최댓값(max_value)을 출력한다.

'''
