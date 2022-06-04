t = int(input())

for tc in range(1, t + 1) :
    n, d = map(int, input().split())
    d = d * 2 + 1
    result = n // d
    if n % d != 0 :
        result += 1

    print('#%d %d' % (tc, result))
    
'''
1. 만약 n이 5이고 d가 1일 경우, 분무기를 한 번 뿌릴 때마다 3개의 꽃에 뿌릴 수 있다.
2. 따라서, d의 값을 (d * 2 + 1)로 갱신하여 분무기를 한 번 뿌릴 때마다 물을 받는 꽃의 개수를 구한다.
3. n을 d로 나눈 값을 result에 할당하고, 만약 나머지 값이 존재한다면 1을 더한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
