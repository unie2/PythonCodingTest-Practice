t = int(input())

for tc in range(1, t + 1) :
    data = input()
    value = 15 - len(data)
    if value < 0 :
        value = 0

    if data.count('o') + value >= 8 :
        print('#%d %s' % (tc, 'YES'))
    else :
        print('#%d %s' % (tc, 'NO'))
        
'''
1. 각 테스트 케이스마다 팔씨름 상황(data)을 입력받고, 15판 중 len(data)판을 제외한 나머지 판들을 소정이가 가져갈 수 있으므로 해당 값을 value에 할당한다.
2. 만약 data 문자열에서 'o'의 개수와 value의 합이 8 이상이라면 소정이가 점심값을 면제 받을 수 있으므로 해당 테스트 케이스 번호와 함께 'YES'를 출력한다.
3. 그렇지 않을 경우 해당 테스트 케이스 번호와 함께 'NO'를 출력한다.

'''
