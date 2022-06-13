t = int(input())

for tc in range(1, t + 1) :
    a, b, c = map(int, input().split())

    print('#%d %d' % (tc, c // min(a, b)))
    
'''
1. 최대로 살 수 있는 빵의 개수를 구하기 위해서는 입력받은 a원 b원 중에 더 작은 값을 구해 해당 빵을 최대로 사면 된다.
2. 따라서 a, b 중 최솟 값을 구하고 c를 최솟값으로 나눈 몫을 출력한다.

'''
