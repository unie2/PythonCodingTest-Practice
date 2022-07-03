for tc in range(1, 11) :
    dump = int(input())
    data = list(map(int, input().split()))

    for _ in range(dump) :
        # 최댓값을 1 감소
        max_pos = data.index(max(data))
        data[max_pos] -= 1
        # 최솟값을 1 증가
        min_pos = data.index(min(data))
        data[min_pos] += 1

    # 최댓값과 최솟값의 차이
    result = max(data) - min(data)

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 dump를 반복문 수행횟수로 지정하고, 각 작업을 아래와 같이 수행한다.
  - data 리스트 내 요소 중 최댓값의 인덱스를 구하여 max_pos에 할당하고, 해당 인덱스에 존재하는 값을 1 감소시킨다.
  - data 리스트 내 요소 중 최솟값의 인덱스를 구하여 min_pos에 할당하고, 해당 인덱스에 존재하는 값을 1 증가시킨다.

2. data 리스트 내 요소 중 최댓값과 최솟값의 차이를 구하여 result에 할당하고, 해당 테스트 케이스 번호와 함께 출력한다.

'''
