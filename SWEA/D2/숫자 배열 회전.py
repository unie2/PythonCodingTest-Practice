t = int(input())

def rotate(a, b) :
    for i in range(n) :
        for j in range(n) :
            b[j][n-1-i] = a[i][j]

for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    degree_90 = [[0] * n for _ in range(n)]
    degree_180 = [[0] * n for _ in range(n)]
    degree_270 = [[0] * n for _ in range(n)]

    rotate(data, degree_90)
    rotate(degree_90, degree_180)
    rotate(degree_180, degree_270)

    print("#%d" % tc)
    for i in range(n) :
        print(''.join(map(str, degree_90[i])), end=' ')
        print(''.join(map(str, degree_180[i])), end=' ')
        print(''.join(map(str, degree_270[i])), end=' ')
        print()
        
'''
1. 각 테스트 케이스마다 n x n 크기의 행렬을 입력받아 data 리스트를 구성한다.
2. n x n 크기로 90도(degree_90), 180도(degree_180), 270도(degree_270) 회전한 값이 담길 리스트를 정의한다.
3. rotate() 함수를 수행하여 두 번째 매개변수 리스트를 갱신한다. 
4. 최종적으로 반복문을 통해 문제에서 요구하는 출력 형식에 맞추어 각 리스트의 값들을 출력한다.

'''
