for tc in range(1, 11) :
    n = int(input())
    data = list(map(int, input().split('+')))

    print('#%d %d' % (tc, sum(data)))
    
'''
1. 각 테스트 케이스마다 입력받은 값을 '+'를 기준으로 구분하여 data 리스트에 저장한다.
2. 해당 테스트 케이스 번호와 함께 data 리스트 내 요소들의 합을 출력한다.

'''
