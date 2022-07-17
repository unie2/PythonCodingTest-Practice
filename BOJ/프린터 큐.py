t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    check = [0 for _ in range(n)]
    check[m] = 1

    count = 0
    while True :
        if priority[0] == max(priority) :
            count += 1
            if check[0] == 1 : # 찾을 값이면
                print(count)
                break
            else :
                priority.pop(0)
                check.pop(0)
        else :
            priority.append(priority.pop(0))
            check.append(check.pop(0))
            
'''
1. 각 테스트 케이스마다 입력받은 n개의 0 값을 저장한 check 리스트를 생성하고, check[m] 을 1로 갱신한다.

2. 아래와 같은 작업을 반복 수행한다.
  - 만약 priority의 가장 첫 번째 요소가 최댓값과 같다면 count를 1증가시킨다.
  - 만약 check의 가장 첫 번째 요소가 1일 경우 찾을 값이므로 count를 출력한 후 break 한다.
  - check[0]이 1이 아닐 경우 priority의 가장 첫 번째 요소와 check의 가장 첫 번째 요소를 빼낸다.

  - 만약 priority[0]이 최댓값이 아닐 경우 priority의 가장 첫 번째 요소와 check의 가장 첫 번째 요소를 각각 빼내어 뒤로 넘겨 준다.

'''
