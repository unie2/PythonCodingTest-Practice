t = int(input())

for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    for i in range(len(data)) :
        if data[i] < 40 :
            data[i] = 40

    sum_value = sum(data)
    avg_value = sum_value // 5

    print('#%d %d' % (tc, avg_value))
    
'''
1. 각 테스트 케이스마다 5개의 점수를 입력받아 data 리스트에 저장하고, 점수를 하나씩 확인하여 40점 미만인 점수는 40점으로 갱신한다.
2. 5개의 점수의 총 합을 sum_value에 할당하고, sum_value를 5로 나눈 몫을 avg_value에 할당한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 avg_value를 출력한다.

'''
