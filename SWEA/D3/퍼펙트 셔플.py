t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = list(input().split())
    if len(data) % 2 == 0 :
        a_list = data[:len(data)//2]
        b_list = data[len(data)//2:]
    else :
        a_list = data[:len(data) // 2 + 1]
        b_list = data[len(data) // 2 + 1:]
    result = []

    while a_list or b_list :
        if a_list :
            result.append(a_list.pop(0))
        if b_list :
            result.append(b_list.pop(0))

    print(f'#{tc}', *result)
    
'''
1. 각 테스트 케이스마다 입력받은 n개의 값을 data 리스트에 저장한다.

2. 만약 data 리스트의 길이가 짝수라면 len(data) // 2 로 설정하여 절반으로 나누고 각 a_list, b_list에 저장한다.

3. 만약 data 리스트의 길이가 홀수라면 len(data) // 2 + 1 로 설정하여 절반으로 나누고 각 a_list, b_list에 저장한다.

4. a_list, b_list 리스트가 모두 빌 때까지 아래와 같은 작업을 반복 수행한다.
  - 만약 a_list 리스트에 요소가 존재한다면 가장 첫 요소 값을 빼내어 result 리스트에 저장한다.
  - 만약 b_list 리스트에 요소가 존재한다면 가장 첫 요소 값을 뺴내어 result 리스트에 저장한다.

5. 최종적으로 해당 테스트 케이스 번호와 함께 result 리스트의 요소를 출력한다.

'''
