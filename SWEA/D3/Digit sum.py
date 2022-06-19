t = int(input())

result = []
for tc in range(1, t + 1) :
    n = input()

    while len(n) != 1 :
        sum_value = 0
        for i in range(len(n)) :
            sum_value += int(n[i])
        n = str(sum_value)

    result.append(n)

for idx, value in enumerate(result) :
    print('#%d %s' % (idx + 1, value))
    
'''
1. 각 테스트 케이스마다 입력받은 수의 길이가 1이 될 때까지 아래와 같은 작업을 반복한다.
  - n의 각 자릿수를 정수형으로 변환하여 sum_value에 누적한다.
  - 모든 자릿수에 대한 누적 작업을 마치면 sum_value를 문자열 형태로 변환하여 n에 갱신한다.

2. 한 자리 수로 정의된 n을 result 리스트에 저장한다.

3. 모든 테스트 케이스에 대한 작업을 마치면 enumerate() 를 통해 해당 테스트 케이스 번호와 함께 값을 출력한다.

'''
