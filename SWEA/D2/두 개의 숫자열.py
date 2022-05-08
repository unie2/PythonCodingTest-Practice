t = int(input())
for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())

    result = 0
    for i in range(abs(n - m) + 1) :
        value = 0
        for j in range(min(n, m)) :
            if len(a) > len(b) :
                value += int(a[j+i]) * int(b[j])
            elif len(a) < len(b) :
                value += int(a[j]) * int(b[j+i])
            else :
                value += int(a[j]) * int(b[j])
        if value > result :
            result = value

    print('#%d %d' % (tc, result))
    
    
'''
1. 각 테스트 케이스마다 두 숫자열을 입력받아 각 리스트 형태로 정의한다.
2. 이중 for문을 통해 서로 마주보는 숫자들을 곱한 뒤 모두 더했을 때의 최댓값 (result)을 구한다. 작업은 아래와 같다.
  - 바깥쪽 for문의 범위는 입력받은 n과 m의 차이에서 1을 더한 값으로 설정한다.
  - 내부 for문의 범위는 입력받은 n과 m 중 작은 값으로 설정한다.
  - 만약 a의 길이가 더 클 경우, int(a[j+i]) * int(b[j]) 를 계산하여 value에 누적한다.
  - 만약 a의 길이가 더 작을 경우, int(a[j]) * int(b[j+i]) 를 계산하여 value에 누적한다.
  - 만약 두 길이가 모두 같다면, 같은 인덱스를 기준으로 두 값을 곱하여 value에 누적한다.
  - 내부 반복문을 통해 갱신된 value 값을 result와 비교하고, value 값이 더 크다면 result 값을 value 값으로 갱신한다.
3. 바깥쪽 반복문 작업이 모두 끝나면 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
