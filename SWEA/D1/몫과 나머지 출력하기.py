t = int(input())

for i in range(1, t + 1) :
    a, b = map(int, input().split())
    print("#%d" % i, end=" ")
    print(a // b, end=" ")
    print(a % b)
    
# 1. a와 b를 입력받아 각 테스트 케이스 번호와 함께 a를 b로 나눈 몫과 나머지 값을 출력 형식에 맞추어 출력한다.
