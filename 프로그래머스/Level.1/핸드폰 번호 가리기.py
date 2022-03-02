def solution(phone_number):
    data = '*' * (len(phone_number) - 4) + phone_number[-4:]
    
    return data
  
  
# 1. phone_number 길이에서 4를 뺀 값만큼의 '*'과 전화번호의 뒷 4자리의 번호를 붙여 문자열 data에 삽입하여 반환한다.
