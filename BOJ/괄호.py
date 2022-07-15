t = int(input())
for _ in range(t) :
    data = list(input())
    open = 0

    for d in data :
        if d == '(' :
            open += 1
        else :
            open -= 1
            if open < 0 :
                print("NO")
                break
    else :
        if open > 0 :
            print("NO")
        else :
            print("YES")
            
'''
1. 입력받은 문자열을 리스트 형태로 저장하고 데이터를 하나씩 꺼내 확인한다.

2. 만약 그 값(d)이 '(' 일 경우 open 값을 1 증가시킨다.

3. 만약 그 값(d)이 ')'일 경우 open 값을 1 감소시키고, open 값이 음수가 되면 "NO"를 출력한 후 break 한다.

4. 반복문이 break 되지 않았다면 open 값을 확인하여 그 값이 0보다 클 경우 올바른 괄호를 이룰 수 없으므로 "NO"를 출력한다.
   open 값이 0이라면 올바른 괄호를 만들 수 있으므로 "YES"를 출력한다.

'''
