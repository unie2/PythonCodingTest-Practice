t = int(input())

for tc in range(1, t + 1) :
    hour, minute, next_hour, next_minute = map(int, input().split())
    result_hour = hour + next_hour

    result_minute = minute + next_minute

    if result_minute > 59 :
        result_hour += 1
        result_minute -= 60

    if result_hour > 12 :
        result_hour -= 12

    print('#%d %d %d' % (tc, result_hour, result_minute))
    
'''
1. 각 테스트 케이스마다 두 시각을 입력받아 시에 해당하는 두 값을 더하여 result_hour에 할당하고, 분에 해당하는 두 값을 더하여 result_minute에 할당한다.
2. result_minute 값이 59보다 클 경우 최종 시 값에 해당하는 result_hour를 1 증가시키고, result_minute 값에서 60을 감소시킨다.
3. result_hour 값이 12보다 클 경우 result_hour 값에서 12를 감소시킨다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 시각(result_hour, result_minute)을 출력한다.

'''
