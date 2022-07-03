for tc in range(1, 11) :
    n = int(input())
    data = list(map(int, input().split()))
    result = 0

    for i in range(2, n - 2) :
        left = max(data[i-1], data[i-2])
        right = max(data[i+1], data[i+2])
        if data[i] - left > 0 and data[i] - right > 0 : # 양 방향의 조망이 모두 확보되면
            max_dir = max(left, right)
            result += data[i] - max_dir

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 값을 입력받아 data 리스트에 저장한다.

2. 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않으므로 2부터 n - 2까지를 반복문의 범위로 설정하여 아래와 같은 작업을 수행한다.
  - 특정 건물(i)을 기준으로 하여 (i-1)건물과 (i-2)건물 중 최댓값을 left에 할당한다.
  - 특정 건물(i)을 기준으로 하여 (i+1)건물과 (i+2)건물 중 최댓값을 right에 할당한다.
  - 만약 data[i] - left 가 0보다 크고 data[i] - right 가 0보다 크다면 양 방향의 조망이 모두 확보되었으므로, left와 right 중 최댓값을 구하여 data[i]에서 뺀 값을 result에 누적한다.

3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
