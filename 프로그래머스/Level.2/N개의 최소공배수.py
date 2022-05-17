def check(arr, target) :
    for i in range(len(arr)) :
        if target % arr[i] != 0 :
            return False
    return True

def solution(arr) :
    value = max(arr)
    add_value = max(arr)
    while True :
        if check(arr, value) :
            return value
        else :
            value += add_value
            
'''
1. 전달받은 arr 리스트에서 가장 큰 값을 value와 add_value에 할당한다.
2. while문을 통해 반복수행하며 반복문 내부에서는 check() 함수를 통해 arr 리스트 내 요소들의 최소 공배수가 성립하면 True를 반환받아 value 값을 출력한다.
3. 만약 arr 리스트 내 요소들의 최소 공배수가 성립되지 않는다면 value에 add_value를 더하여 반복 작업을 계속한다.

'''
