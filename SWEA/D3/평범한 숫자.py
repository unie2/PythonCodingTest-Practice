t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(1, n - 1) :
        left, right = data[i-1], data[i+1]
        if data[i] != min(left, right, data[i]) and data[i] != max(left, right, data[i]) :
            result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 수를 입력받아 data 리스트에 저장한다.
2. 1번째 요소부터 n - 2번째 요소를 각 확인하며, 각 인덱스의 이전 data 값과 이후 data 값을 left, right에 할당한다.
3. 만약 현재의 값(data[i])이 left, right, data[i] 중 최솟값도, 최댓값도 아니라면 result를 1 증가시킨다.
4. 반복 수행이 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result를 출력한다.

'''
