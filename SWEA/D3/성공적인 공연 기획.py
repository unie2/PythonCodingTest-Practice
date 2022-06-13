t = int(input())

for tc in range(1, t + 1) :
    data = list(str(input()))
    clap = 0
    result = 0

    for i in range(len(data)) :
        if data[i] != 0 :
            if clap >= i :
                clap += int(data[i])
            else :
                result += i - clap
                clap = i + int(data[i])

    print('#%d %d' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력받은 문자열 data의 문자를 하나씩 확인한다.

2. 만약 현재 값이 0이 아닐 경우 아래와 같은 작업을 수행한다.
  - 만약 clap 값이 i보다 크거나 같다면 단순히 현재의 값을 clap에 누적한다.
  - 그렇지 않을 경우 사람을 고용해야하므로 result에 i - clap (부족한 인원) 을 누적하고 clap 값을 갱신한다.

3. 최종적으로 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
