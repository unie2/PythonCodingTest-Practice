t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(map(int, input().split()))
    result = 1e9

    for i in range(7) :
        if data[i] == 1 :
            index = i
            temp_n = n
            temp_result = 0
            while temp_n :
                if data[index] == 1 :
                    temp_n -= 1
                temp_result += 1
                index = (index + 1) % 7

            if result > temp_result :
                result = temp_result

    print('#%d %d' % (tc, result))
    
'''
1. 만약 특정 요일에 수업을 듣는지의 여부가 담긴 data 리스트가 [1, 0, 0, 0, 1, 0, 1] 이고, 수업을 들어야 하는 일 수 n이 2일 경우를 보면,
  - 0번째 요소에서 시작하면 지내야 하는 일 수가 5 가 된다.
  - 4번째 요소에서 시작하면 지내야 하는 일 수가 3 이 된다.
  - 6번째 요소에서 시작하면 지내야 하는 일 수가 2 가 된다.
  - 이와 같이 수행하면 지내야 하는 최소 일 수는 2가 되어야 한다. 따라서, 이러한 상황을 모두 확인하여 최솟 값을 갱신하는 방식으로 진행한다.

2. 최솟 값을 담기 위한 result의 초기 값은 1e9로 설정한다.

3. data 리스트의 요소를 하나씩 확인하여 해당 인덱스의 값이 1일 경우 index를 해당 인덱스로 설정하고, temp_n에 임시로 n 값을 담는다.

4. while문을 통해 temp_n이 0이 될 때까지 아래와 같이 수행한다.
  - 만약 현재 index의 data 값이 1일 경우 temp_n 값을 1 감소시킨다.
  - 지내야 하는 일 수를 의미하는 temp_result를 1 증가시키고 다음 요일을 확인하기 위해 index를 갱신한다.

5. 만약 현재의 temp_result 값이 result 값보다 작을 경우 temp_result를 result에 갱신한다.

6. 모든 상황을 판별한 후 최종적으로 해당 테스트 케이스 번호와 함께 result 를 출력한다.

'''
