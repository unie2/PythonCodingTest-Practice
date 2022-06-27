t = int(input())

for tc in range(1, t + 1) :
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    result = "Possible"
    for i in range(n) :
        # people[i] 초까지 만들어진 붕어빵의 개수
        cnt = (people[i] // m) * k - (i + 1)
        if cnt < 0 :
            result = "Impossible"
            break

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 n개의 정수를 입력받아 people 리스트에 저장하고, 오름차순으로 정렬한다.

2. result의 초기 값으로 "Possible"을 할당하고, 아래와 같이 반복 작업을 수행한다.
  - people[i] 초까지 만들어진 붕어빵의 개수를 구한다. 이때 (i + 1)을 빼준 이유는 이전까지의 손님들에게 붕어빵을 팔았기 때문이다.
  - 만약 cnt 값이 0 미만이라면 손님이 기다려야 붕어빵을 제공받을 수 있다는 의미이므로 result 값을 "Impossible"로 갱신하고 break 한다.

3. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
