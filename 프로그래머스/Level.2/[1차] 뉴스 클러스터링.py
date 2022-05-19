def solution(str1, str2) :
    update_str1 = []
    for i in range(len(str1) - 1) :
        if str1[i].isalpha() and str1[i+1].isalpha() :
            temp_str1 = str1[i:i+2].lower()
            update_str1.append(temp_str1)

    update_str2 = []
    for i in range(len(str2) - 1) :
        if str2[i].isalpha() and str2[i+1].isalpha() :
            temp_str2 = str2[i:i+2].lower()
            update_str2.append(temp_str2)

    sum_len = len(update_str1) + len(update_str2)

    intersection = [] # 교집합
    if len(update_str1) < len(update_str2) :
        for i in range(len(update_str1)) :
            if update_str1[i] in update_str2 :
                intersection.append(update_str1[i])
                update_str2.pop(update_str2.index(update_str1[i]))
    else :
        for i in range(len(update_str2)) :
            if update_str2[i] in update_str1 :
                intersection.append(update_str2[i])
                update_str1.pop(update_str1.index(update_str2[i]))

    union = sum_len - len(intersection) # 합집합

    if sum_len == 0 :
        answer = 65536
    else :
        answer = int((len(intersection) / union) * 65536)
    return answer
  
'''
1. 각 str1, str2 문자열에 존재하는 문자를 하나씩 확인하여 해당 문자와 다음 문자가 영문자일 경우 update_str1 혹은 update_str2에 두 문자를 소문자로 변환하여 추가한다.
2. update_str1의 길이와 update_str2의 길이를 더하여 sum_len에 할당한다.
3. 길이가 더 작은 것을 기준으로 하여 해당 문자열이 다른 리스트에 존재한다면 intersection 리스트에 해당 문자열을 추가하고 다른 리스트에서 해당 문자열을 제거한다.
4. sum_len에서 교집합(intersection) 길이를 빼낸 합집합 개수를 union에 할당한다.
5. 만약 sum_len이 0일 경우 두 집합 모두 공집합이므로 단순히 65536을 answer에 할당하고, 0이 아닐 경우 (교집합 개수 / 합집합 개수) * 65536 을 정수형으로 변환하여 answer에 할당한다.
6. 최종적으로 answer 값을 반환한다.

'''
