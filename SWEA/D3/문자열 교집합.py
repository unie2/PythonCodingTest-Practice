t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    origin_count = n + m
    data_n = list(input().split())
    data_m = list(input().split())
    data = data_m + data_n
    result = origin_count - len(set(data))

    print('#%d %d' % (tc, result))
    
    
'''
1. 각 테스트 케이스마다 입력받은 n, m을 통해 총 문자열의 개수(n + m)를 구해 origin_count에 할당한다.
2. 문자열들을 입력받아 합치고, 중복을 제거한 후의 문자열 개수를 origin_count에서 뺀 값을 result에 할당한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
