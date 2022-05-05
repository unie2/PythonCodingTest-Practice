t = int(input())
for i in range(1, t + 1) :
    n = int(input())
    num = [2, 3, 5, 7, 11]
    result = [0] * 5
    while True :
        for j in range(5) :
            while True :
                if n % num[j] == 0 :
                    n //= num[j]
                    result[j] += 1
                else :
                    break
        if n == 1 :
            break

    print('#%d' % i, end=' ')
    for j in range(5) :
        print(result[j], end=' ')
    print()
    
'''
1. 각 테스트 케이스마다 n을 입력받고, [2, 3, 5, 7, 11]을 담은 num 리스트와 5개의 0으로 이루어진 result 리스트를 정의한다.
2. n의 값이 1이 될 때까지 반복문을 수행하며, 내부 작업은 아래와 같다.
  - num에 담겨 있는 요소를 하나씩 확인하여 현재의 n 값을 num[j]로 나누어 떨어지면 n을 num[j]로 나눈 값으로 갱신하고 result[j]의 값을 1 증가시킨다.
3. 위 반복 수행이 종료되면 현재 테스트 케이스 번호와 함께 result 리스트 내 값들을 하나씩 출력한다.

'''
