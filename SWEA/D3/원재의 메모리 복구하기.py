t = int(input())

for tc in range(1, t + 1) :
    target = input()
    data = ['0'] * len(target)
    result = 0

    for i in range(len(data)) :
        if data[i] != target[i] :
            if data[i] == '0' :
                value = '1'
            else :
                value = '0'
            for j in range(i, len(data)) :
                data[j] = value
            result += 1

        if ''.join(data) == target :
            break

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 메모리 값의 길이만큼 '0'으로 구성하여 리스트로 data에 정의한다.

2. data 리스트의 요소를 순서대로 하나씩 확인하고, 해당 값과 target 문자열의 같은 인덱스에 존재하는 값이 다를 경우 아래와 같은 작업을 수행한다.
  - 만약 data 리스트의 해당 값이 '0'일 경우 value에 '1'을 할당하고, 그렇지 않을 경우 value에 '0'을 할당한다.
  - 해당 인덱스부터 끝까지 data 리스트의 각 값을 모두 value로 갱신한다.
  - result 값을 1 증가시킨다.

3. 만약 data를 문자열로 변환한 값과 target 문자열이 같을 경우 break 한다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
