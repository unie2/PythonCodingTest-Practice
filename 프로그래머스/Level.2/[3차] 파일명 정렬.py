def solution(files) :
    answer = []

    for file in files :
        head, number, tail = '', '', ''

        check = False
        for i in range(len(file)) :
            if file[i].isdigit() :
                number += file[i]
                check = True
            elif not check :
                head += file[i]
            else :
                tail = file[i:]
                break

        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(value) for value in answer]
    return answer
  
'''
1. files 리스트 내 문자열을 하나씩 꺼내고, 해당 문자열의 문자를 하나씩 확인한다.
2. 문자가 숫자일 경우 number 문자열에 해당 문자를 추가하고 check를 True로 갱신한다.
3. 문자가 숫자가 아니고 이전에 숫자가 나온적도 없다면 head 문자열에 해당 문자를 추가한다.
4. 이전에 숫자가 나온적이 있고 현재 확인하고 있는 값이 문자일 경우 현재 문자부터 끝까지 tail에 할당한 후 break한다.
5. 반복문이 끝난 후 정의된 (head, number, tail)을 튜플 형태로 하여 answer 리스트에 추가한다.
6. files의 문자열 작업을 모두 처리하면 answer 리스트를 정렬한다. 여기서 head를 소문자로 변경한 값을 우선으로 하고, head가 같다면 number을 정수형으로 변환하여 우선한다.
7. 하나의 문자열이 나눠져 있는 answer 리스트의 요소를 붙여서 갱신한 후 최종적으로 answer를 반환한다.

'''
