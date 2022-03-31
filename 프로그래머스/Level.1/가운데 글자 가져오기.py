def solution(s):
    answer = ''
    if len(s) % 2 == 0 :
        index = len(s) // 2 -1
        answer += s[index:index+2]
    else :
        index = len(s) // 2
        answer += s[index]
        
    return answer
  
'''
1. 단어 s의 길이를 확인하여 길이가 짝수라면 가운데를 기준으로 왼쪽 인덱스 값(len(s) // 2 -1)을 구한 후 가져올 글자의 범위를 s[index:index+2]로 지정하여 두글자를 반환한다.
2. 단어 s의 길이가 홀수라면 단순히 단어의 길이의 절반을 index 값으로 구한 후 해당 위치의 글자를 반환한다.

'''
