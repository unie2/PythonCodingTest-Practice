t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    max_value = data[0]

    for i in range(n-1) :
        if data[i] >= 0 and (data[i] + data[i+1]) >= 0 :
            data[i+1] += data[i]
        if data[i+1] > max_value :
            max_value = data[i+1]

    print('#%d %d' % (tc, max_value))
    
'''
1. n개의 정수값을 입력받아 data 리스트에 할당하고 가장 첫번째 값을 max_value에 할당한다.
2. 반복문을 통해 만약 현재의 값이 음수가 아니고 다음 값과 더한 값도 음수가 아닐 경우 두 수의 합을 다음 값에 할당한다.
3. 이후 다음 값(data[i+1])이 max_value 보다 크다면 max_value를 해당 값으로 갱신한다.
4. 반복문이 종료되면 최종적으로 해당 테스트 케이스 번호와 함께 max_value 값을 출력한다.

'''
