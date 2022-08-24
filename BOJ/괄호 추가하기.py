def func(i, q) :
    if i == n - 1 :
        no_use = q + [data[i]]
        return cal_q(no_use)
    if i == n - 3 :
        no_use = q + [data[i], data[i+1]]
        temp = cal_num(data[i], data[i+2], data[i+1])
        use = q + [temp]
        return max(func(i+2, no_use), cal_q(use))
    # 미포함
    no_use = q + [data[i], data[i+1]]
    # 포함
    temp = cal_num(data[i], data[i+2], data[i+1])
    use = q + [temp, data[i+3]]

    return max(func(i+2, no_use), func(i+4, use))

def cal_q(queue) :
    result = queue[0]
    for i in range(0, len(queue)-2, 2) :
        next = queue[i+2]
        result = cal_num(result, next, queue[i+1])
    return result

def cal_num(target, next, oper) :
    if oper == '+' :
        return target + next
    elif oper == '-' :
        return target - next
    elif oper == '*' :
        return target * next

n = int(input())
data = [int(x) if x != '+' and x != '-' and x != '*' else x for x in input()]

print(func(0, []))

'''
1. 괄호를 포함한 계산 식과 포함하지 않은 계산 식을 비교하여 더 큰 값을 반환함으로써 문제를 해결할 수 있다.

2. 입력받은 연산자 및 피연산자를 data 리스트에 담은 후 func() 함수를 호출하여 아래와 같은 작업을 수행하고, 반환받은 값을 출력한다.
  - 만약 i가 n-1 과 같다면, 즉 마지막 요소일 경우 현재의 q에 data[i]를 추가하고, 이를 매개변수로 하여 cal_q() 함수를 호출한 후 반환받은 값을 반환한다.
  - 만약 i가 n-3과 같다면 괄호를 포함하지 않는 변수(no_use)에 q + [data[i], data[i+1]]를 담는다.
    또한, 괄호를 포함한 값을 구하기 위해 cal_num(data[i], data[i+2], data[i+1])을 통해 반환받은 값을 q에 추가하여 use를 정의한다.
  - func(i+2, no_use) 와 cal_q(use)를 비교하여 더 큰 값을 반환한다.
 
  - i가 n-1도 아니고 n-3도 아닌 경우 괄호를 미포함한 연산식(no_use)과 괄호를 포함한 연산식(use)을 정의한다.
  - func(i+2, no_use) 와 func(i+4, use) 를 비교하여 더 큰 값을 반환한다.

3. cal_q(queue) 함수의 작업은 아래와 같다.
  - result에 queue의 첫 번째 수를 할당한다.
  - for문 내부에서는 queue[i+2]를 next에 담은 후 cal_num() 함수를 호출하여 result와 next 간의 연산 작업을 수행한 값을 result에 할당한다.
  - 반복 수행이 종료되면 result 를 반환한다.

4. cal_num(target, next, oper) 함수의 작업은 아래와 같다.
  - oper가 '+'일 경우 target + next 값을 반환한다.
  - oper가 '-'일 경우 target - next 값을 반환한다.
  - oper가 '*'일 경우 target * next 값을 반환한다.

'''
