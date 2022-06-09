t = int(input())

def check(value) :
    value = str(value)
    for i in range(len(value) - 1) :
        if value[i] > value[i+1] :
            return False
    return True

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))

    result = 0
    for i in range(n - 1) :
        for j in range(i+1, n) :
            value = data[i] * data[j]
            if check(value) :
                result = max(result, value)
        if result == 0 :
            result = -1

    print(f'#{tc} {result}')
    
'''
1. 각 테스트 케이스마다 n개의 값을 입력받아 data 리스트에 저장한다.

2. n-1을 반복문 i의 범위로 설정하고, i+1부터 n까지를 반복문 j의 범위로 설정하여 data[i] * data[j] 의 값을 value에 할당한다.

3. check() 함수를 통해 단조 증가하는 수인지 확인하고, True를 반환받았다면 value 값과 result 값을 비교하여 더 큰 값을 result에 갱신한다.

4. 만약 단조 증가하는 수가 없다면 -1을 result에 할당한다.

5. 단조 증가하는 수인지 확인하는 check() 함수의 작업은 아래와 같다.
  - 전달받은 value 값을 문자열 형식으로 변환하여 재정의한다.
  - 문자를 하나씩 확인하여 만약 value[i]가 value[i+1]보다 크다면 단조 증가하는 수가 아니므로 False를 반환한다.
  - 반복문이 끝날 때까지 False가 반환되지 않았다면 True를 반환한다.

6. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
