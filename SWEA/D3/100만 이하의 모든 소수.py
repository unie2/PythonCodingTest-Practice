n = 10 ** 6 + 1
data = [1] * n
data[0], data[1] = 0, 0

# 배수 처리
for i in range(2, n) :
    if data[i] == 1 :
        for j in range(i * 2, n, i) :
            data[j] = 0

for i in range(n) :
    if data[i] == 1 :
        print(i, end=' ')
        
'''
1. 문제에서 주어진 범위만큼의 길이를 가진 data 리스트의 요소들을 모두 1로 초기화한다.
2. data[0], data[1] 의 값은 소수가 아니므로 0으로 갱신한다.
3. 2부터 n까지를 범위로 하여 data[i]가 1일 경우(소수일 경우) 해당 수의 배수를 모두 0으로 갱신한다.
4. data 리스트에 존재하는 값이 1인 경우에만 해당 수를 출력한다.

'''
