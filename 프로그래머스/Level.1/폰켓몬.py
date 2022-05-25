def solution(nums) :
    set_nums = set(nums)
    if len(set_nums) >= len(nums) // 2 :
        answer = len(nums) // 2
    else :
        answer = len(set_nums)

    return answer
  
'''
1. 전달받은 nums 리스트의 중복을 제거하여 set_nums에 할당한다.
2. 만약 set_nums의 길이가 nums의 길이를 2로 나눈 값보다 크거나 같다면 answer에 len(nums) // 2 를 할당한다.
3. 그렇지 않다면 set_nums의 길이를 answer에 할당한다.

'''
