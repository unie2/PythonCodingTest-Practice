def dfs(index, count) :
    global result
    if count == int(cnt) :
        result = max(int(''.join(data)), result)
        return
    for now in range(index, len(data)) :
        for max_idx in range(now + 1, len(data)) :
            if data[now] <= data[max_idx] :
                data[now], data[max_idx] = data[max_idx], data[now]
                dfs(now, count + 1)
                data[now], data[max_idx] = data[max_idx], data[now]

    if result == 0 and count < int(cnt) :
        extra = (int(cnt) - count) % 2
        # 짝수라면 그대로, 홀수라면 한 번 변경
        if extra == 1 : # 홀수라면
            data[-1], data[-2] = data[-2], data[-1]
        dfs(index, int(cnt))

t = int(input())

for tc in range(1, t + 1) :
    data, cnt = input().split()
    data = list(data)
    result = 0
    dfs(0, 0)

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 dfs() 함수를 호출하고, 최종적으로 갱신된 result 값을 해당 테스트 케이스 번호와 함께 출력한다.

2. dfs() 함수의 작업은 아래와 같다.
  - 만약 전달받은 count값이 입력받은 cnt 값과 같다면 현재의 data리스트의 요소를 붙인 정수값과 result 값을 비교하여 더 큰 값을 result에 할당하고 return 한다.
  - 2중 for문을 통해 작업을 수행하며, 만약 data[now] 값이 data[max_idx] 이하일 경우 두 값을 교환하고 dfs() 함수를 재귀 호출한다.
   재귀 호출 후에는 다른 경우를 확인하기 위해 다시 교환해준다.

  - 반복문이 끝난 후 만약 result 값이 0 이고 교환 횟수가 아직 남았다면 남은 횟수를 2로 나눈 나머지 값을 구해 extra에 할당한다.
  - 만약 extra가 짝수라면 그대로 두고, 홀수라면 마지막 요소 두개를 한 번 교환한다.
  - 이후 index와 cnt 값을 매개변수로 하여 dfs() 함수를 호출한다.

'''
