t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    result = []
    data = input()

    start = 0
    for i in range(len(data)) :
        if data[i] in ['.', '?', '!'] :
            cnt = 0
            for value in data[start:i].split() :
                if (len(value) == 1 and value[0].isupper()) or (value[0].isupper() and value.isalpha() and value[1:].islower()) :
                    cnt += 1
            start = i + 2

            result.append(cnt)

    print(f'#{tc}', *result)
    
'''
1. 각 테스트 케이스마다 입력받은 문자열의 문자를 하나씩 확인한다.
2. 해당 문자가 '.' 혹은 '?' 혹은 '!' 이라면 data[start:i]의 문자열을 공백으로 구분하여 한 부분씩 확인한다.
3. 만약 (문자열 value의 길이가 1이고 대문자) 이거나 (value의 첫 문자가 대분자이고 숫자가 삽입되어있지 않고, 두 번째 문자부터 모두 소문자) 라면 cnt를 1 증가시킨다.
4. 이후 start를 i + 2 (세 가지 구두점 이후에는 공백이 포함되므로) 값으로 갱신하고, result 리스트에 cnt를 추가한다.
5. 입력받은 문자열(data)에 대한 문자를 모두 확인하면 최종적으로 해당 테스트 케이스 번호와 함께 result에 존재하는 값들을 출력한다.

'''
