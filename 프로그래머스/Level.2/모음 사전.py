from itertools import product

def solution(word) :
    target = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6) :
        arr += list(map("".join, product(target, repeat=i)))

    arr.sort()

    for i in range(len(arr)) :
        if arr[i] == word :
            return i + 1
          
'''
1. 알파벳 'A', 'E', 'I', 'O', 'U' 를 담은 target 리스트를 정의하고, 사전을 만들기 위해 arr 리스트를 정의한다.
2. 1부터 6까지를 반복문의 범위로 설정하여 itertools.product() 모듈을 통해 중복 순열을 수행하여 arr 리스트에 추가한다.
3. 이후 arr리스트를 오름차순으로 정렬하고 값을 하나씩 확인하여 해당 문자열이 word와 같을 경우 해당 인덱스 번호를 반환한다.

'''
