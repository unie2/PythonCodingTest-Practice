t = int(input())

for i in range(1, t + 1) :
    data = list(map(int, input().split()))
    sum_value = sum(data)
    avg_value = sum_value // 10
    if sum_value % 10 >= 5 :
        avg_value += 1

    print('#%d %d' % (i, avg_value))
    
'''
1. 각 테스트 케이스마다 10개의 수를 입력받아 리스트 형태로 구성한다.
2. data 리스트 내 모든 요소들의 합을 구하여 sum_value에 할당하고, sum_value를 10으로 나눈 값을 avg_value에 할당한다.
3. 반올림 작업을 위해 sum_value를 10으로 나눈 나머지 값을 확인하고, 그 값이 5 이상일 경우 avg_value에 1을 더한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 평균 값을 출력한다.

'''
