def solution(n, words) :
    turn = 1 # 처음 순서
    before = words[0][-1]
    for i in range(1, len(words)) :
        # 단어의 시작이 잘못 되었거나 이전에 이미 말한적이 있다면
        if words[i][0] != before or words[i] in words[:i] :
            a, b = divmod(i, n) # 몫, 나머지
            return [b + 1, a + 1]
        else :
            before = words[i][-1]

    return [0, 0]
  
'''
1. 처음 순서는 1번 사람부터 시작하므로 turn에 1을 할당한다.
2. 이전 단어의 끝 문자를 의미하는 before의 초기 값은 words 리스트의 가장 첫 문자열의 첫 문자로 정의한다.
3. words 리스트의 두 번째 요소부터 확인하며, 만약 문자의 시작이 잘못 되었거나 이전에 이미 말한적이 있다면 몫과 나머지를 구해 [b + 1, a + 1] 형태로 반환한다.
4. 정상적으로 말할 수 있다면 before에 현재 문자열의 끝 문자를 할당한다.
5. 주어진 단어들로 탈락자가 생기지 않는다면 [0, 0]을 반환한다.

'''
