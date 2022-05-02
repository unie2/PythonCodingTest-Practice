t = int(input())

for _ in range(t) :
    tc = int(input())
    score = list(map(int, input().split()))
    data = [0] * 1001

    for i in score :
        data[i] += 1

    max_value = max(data)
    result = []
    for i in range(len(data)) :
        if data[i] == max_value :
            result.append(i)

    print('#%d %d' % (tc, max(result)))
    
'''
1. 각 테스트 케이스마다 테스트 케이스의 번호를 입력받고 1000개의 점수를 입력받아 리스트 형태로 구성한다.
2. 0이 1001개 담겨 있는 data 리스트를 정의하고 반복문을 통해 score의 값을 하나씩 확인하여 그 값을 인덱스로 하여 data리스트의 해당 인덱스 값을 1씩 증가시킨다.
3. 반복 작업을 마치면 data 리스트 내 값들 중 최대 값을 구하여 max_value에 할당하고 여러 개의 최빈 값을 담기 위한 result 리스트를 정의한다.
4. 반복문을 통해 data 리스트의 요소를 하나씩 확인하여 그 값이 max_value와 같다면 result에 추가한다.
5. 반복 작업을 마치면 최종적으로 입력받은 테스트 케이스 번호(tc)와 함께 result 리스트 내 값들 중 최대 값을 출력한다.

'''
