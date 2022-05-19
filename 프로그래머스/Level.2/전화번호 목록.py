def solution(phone_book) :
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        index = len(phone_book[i])
        if phone_book[i] in phone_book[i+1][:index] :
            return False

    return True
  
'''
1. 전달받은 phone_book문자열 리스트를 오름차순으로 정렬한다.
2. 정렬된 리스트의 문자열을 하나씩 확인하여 해당 문자열이 다음 문자열 접두사에 존재할 경우 False를 반환한다.
3. 모든 문자열을 확인하면서 False가 반환되지 않았다면 True를 반환한다.

'''
