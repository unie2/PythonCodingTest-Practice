t = int(input())

for i in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = 0
    for j in range(len(data)) :
        if data[j] % 2 == 1 :
            result += data[j]

    print('#%d %d' % (i, result))
    
'''
1. 각 테스트 케이스마다 10개의 수를 입력받아 리스트 형태로 구성한다.
2. 입력받은 값을 하나씩 확인하여 그 값이 홀수라면 result에 그 값을 누적한다.
3. 반복 작업을 마치면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
