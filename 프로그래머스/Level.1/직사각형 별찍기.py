n, m = map(int, input().split())

for i in range(m) :
    for j in range(n) :
        print('*', end='')
    print()
    
    
# 1. 이중 for문을 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태로 '*'을 출력한다.
# 2. 내부 반복문에서 '*'이 n번 출력완료되면 줄바꿈을 해줌으로써 문제에서 요구하는 형태로 해결할 수 있다.
