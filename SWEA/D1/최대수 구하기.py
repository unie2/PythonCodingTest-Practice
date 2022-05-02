t = int(input())

for i in range(1, t + 1) :
    data = list(map(int, input().split()))
    print('#%d %d' % (i, max(data)))
    
'''
1. 각 테스트 케이스마다 10개의 수를 입력받아 리스트 형태로 구성한다.
2. 해당 테스트 케이스 번호와 함께 data 리스트의 값 중 최대 값을 출력한다.

'''
