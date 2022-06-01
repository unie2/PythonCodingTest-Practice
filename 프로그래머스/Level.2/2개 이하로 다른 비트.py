def solution(numbers) :
    answer = []
    for number in numbers :
        bin_num = list('0' + bin(number)[2:])
        index = ''.join(bin_num).rfind('0')
        bin_num[index] = '1'

        if number % 2 == 1 :
            bin_num[index+1] = '0'

        answer.append(int(''.join(bin_num), 2))

    return answer
  
'''
1. numbers에 존재하는 수를 하나씩 가져와 이진수로 변환하고 가장 첫 요소에 '0'을 추가해 리스트 형태로 bin_num에 할당한다.
2. bin_num에서 가장 오른쪽에서 '0'을 찾아 index에 할당하고 bin_num[index]를 '1'로 갱신한다.
   10진수 number 값이 짝수일 경우 다음 숫자가 나오려면 가장 마지막 요소의 '0'을 '1'로 바꾸면 된다. (ex. 4 (100) -> 5 (101))
3. 만약 number 값이 홀수라면 index 다음 위치에 존재하는 값을 '0'으로 갱신한다. (ex. 5 (101) -> 6 (110)
4. 2진수 형태의 bin_num을 10진수로 변환하여 answer 리스트에 추가한다.

'''
