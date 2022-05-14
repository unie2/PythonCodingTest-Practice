n = int(input())

for i in range(1, n + 1) :
    if len(str(i)) < 2 :
        if i in [3, 6, 9] :
            print('-', end=' ')
        else :
            print(i, end=' ')
    else :
        value = ''
        for j in range(len(str(i))) :
            if int(str(i)[j]) == 3 or int(str(i)[j]) == 6 or int(str(i)[j]) == 9 :
                value += '-'

        if len(value) >= 1 :
            print(value, end=' ')
        else :
            print(i, end=' ')
            
'''
1. 1부터 n까지의 숫자를 확인하는데, 만약 확인하고 있는 숫자가 한자리 수일 경우 단순히 [3, 6, 9] 가 있는지 확인하고, 있다면 '-'를 출력하고 없다면 숫자를 그대로 출력한다.

2. 만약 숫자가 두 자리 수 이상일 경우 아래와 같이 작업을 수행한다.
  - 숫자를 문자형으로 변환하여 한 자리 수씩 확인한다.
  - 해당 문자 수를 정수형으로 변환한 값이 3이거나 6이거나 9일 경우 value에 문자 '-'를 추가한다.
  - 모든 문자를 확인하면 최종적으로 value의 길이를 확인해 '-' 문자가 하나라도 있을 경우 value를 출력하고, 없을 경우 숫자(i)를 출력한다.

'''
