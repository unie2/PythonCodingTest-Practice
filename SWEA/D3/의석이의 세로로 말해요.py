t = int(input())

for tc in range(1, t + 1) :
    count = 0
    data = []
    for _ in range(5) :
        str_value = input()
        count += len(str_value)
        data.append(list(map(str, str_value)))

    result = ""
    index = 0
    while count :
        if data[index] :
            result += data[index].pop(0)
            count -= 1
            index = (index + 1) % 5
        else :
            index = (index + 1) % 5

    print('#%d %s' % (tc, result))
    
'''
1. 각 테스트 케이스마다 입력된 문자열을 data 리스트에 저장하고, 모든 문자열의 길이를 count에 정의한다.

2. count가 0이 될 때까지 while문을 수행하며, 만약 data[index]에 값이 존재한다면 가장 첫 문자를 빼내 result에 이어붙인다.
   이후 count를 1 감소시키고 다음 문자를 확인하기 위해 index 값을 갱신한다.

3. 만약 data[index]에 값이 존재하지 않는다면 index만 갱신해준다.

4. 최종적으로 해당 테스트 케이스 번호와 함께 result 문자열을 출력한다.

'''
