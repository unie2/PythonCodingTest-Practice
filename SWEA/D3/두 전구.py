t = int(input())
result = []
for tc in range(1, t + 1) :
    a, b, c, d = map(int, input().split())
    x_list = [0] * (max(a, b, c, d))
    y_list = [0] * (max(a, b, c, d))

    on = 0
    for i in range(a, b) :
        x_list[i] = 1
    for i in range(c, d) :
        y_list[i] = 1

    for a, b in zip(x_list, y_list) :
        if a and b :
            on += 1

    result.append(on)


for idx, value in enumerate(result) :
    print('#%d %d' % (idx + 1, value))
    
'''
1. 각 테스트 케이스마다 x_list와 y_list를 (a, b, c, d) 중 최대값 길이로 설정하여 0으로 초기화한다.
2. 각 a~b, c~d 를 반복문의 범위로 하여 x_list 혹은 y_list의 해당 인덱스의 값을 1로 갱신한다.
3. 두 리스트를 zip()으로 감싼 형태에서 원소를 꺼내 두 값이 모두 1일 경우 on을 1 증가시키고, 모든 원소를 확인하면 갱신된 on을 result에 추가한다.
4. 모든 테스트 케이스에 대한 작업이 끝나면 enumerate() 를 통해 (idx + 1, value) 형태로 값을 출력한다.

'''
