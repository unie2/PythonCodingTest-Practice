def check(arr, cnt) :
    global n, result
    if cnt == n :
        result += 1
        return
    temp = [0] * n
    for i in range(len(arr)) :
        # 열
        temp[arr[i]] = 1
        # 왼쪽 대각선
        if arr[i] - (cnt - i) >= 0 : # 범위 내에 있다면
            temp[arr[i] - (cnt-i)] = 1
        # 오른쪽 대각선
        if arr[i] + (cnt - i) < n : # 범위 내에 있다면
            temp[arr[i] + (cnt-i)] = 1

    for i in range(n) :
        if temp[i] == 0 : # 빈 칸이라면
            check(arr + [i], cnt + 1)

t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = 0
    check([], 0)

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 check() 함수를 호출하여 result 값을 구하여 해당 테스트 케이스 번호와 함께 출력한다.

2. check() 함수의 작업은 아래와 같다.
  - 만약 전달받은 cnt 값과 입력받은 n이 같을 경우 마지막 행까지 퀸을 다 놓은 것이므로 result 값을 1 증가시킨 후 반환한다.
  - n개의 0으로 초기화된 temp 리스트를 정의한다.
  - arr 리스트의 값을 하나씩 꺼내 해당 값을 temp 리스트의 인덱스로 하여 1로 갱신한다.
  - 왼쪽 대각선, 오른쪽 대각선 또한 범위를 벗어나지 않는다면 해당 위치를 1로 갱신한다.
 
  - temp 리스트 요소를 순서대로 확인하면서 해당 인덱스의 값이 0이라면 check() 함수를 재귀호출한다.
  - 이때 arr 리스트에 해당 인덱스를 포함시키고, cnt 값을 1 증가시켜 전달한다.

'''
