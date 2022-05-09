t = int(input())
for i in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    print('#%d' % i, end=' ')
    for j in range(n) :
        print(data[j], end=' ')
    print()
    
'''
1. 각 테스트 케이스마다 n개의 숫자를 입력받아 오름차순으로 정렬한다.
2. 해당 테스트 케이스 번호와 함께 data 리스트 요소들을 하나씩 꺼내 값을 출력한다.

'''
