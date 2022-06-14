t = int(input())

for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)

    result = 0
    for _ in range(k) :
        result += score.pop(0)

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 점수를 입력받아 score 리스트에 저장하고, 내림차순으로 정렬한다.
2. 반복문을 k번으로 설정하고, 각 작업마다 result에 score 리스트의 가장 첫 요소 값을 누적한다.
3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
