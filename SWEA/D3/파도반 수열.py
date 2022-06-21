t = int(input())

data = [1, 1, 1]
for i in range(3, 101) :
    data.append(data[i-2] + data[i-3])

for tc in range(1, t + 1) :
    n = int(input())

    print('#%d %d' % (tc, data[n-1]))
    
'''
1. [1, 1, 1] 을 담은 data 리스트를 정의하고 3부터 101까지를 반복문의 범위로 설정하여 각 data[i-2] + data[i-3] 을 계산하여 data 리스트에 추가한다.
2. 각 테스트 케이스마다 n을 입력받아 해당 테스트 케이스 번호와 함께 data[n-1] 을 출력한다.

'''
