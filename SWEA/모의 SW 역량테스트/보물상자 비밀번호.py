t = int(input())

for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    data = input()
    arr = []
    for j in range(n // 4) :
        for i in range(0, n, n // 4) :
            arr.append(data[i:i+(n//4)])

        data = data[-1] + data[:-1]
    arr = list(set(arr))
    arr.sort(reverse=True)

    result = arr[(k-1) % len(arr)]

    print('#%d %d' % (tc, int(result, 16)))
    
'''
1. 각 테스트 케이스마다 n개의 16진수를 문자열 형태로 입력받는다.
2. 입력되는 n은 4의 배수이고, 보물 상자의 뚜겅을 한 칸씩 회전할 때 가장 처음 상태와 n // 4 번 회전한 이후의 상태와 같다.
3. 따라서 n // 4 를 반복문의 범위로 지정해주고 그 내부에서는 n // 4 개씩 문자를 잘라 arr 리스트에 추가한다.
4. 이후 arr 리스트 내 요소에서 중복을 제거하고 내림차순으로 정렬한다.
5. 정렬이 완료된 arr 리스트의 k 번째 요소를 result에 할당하고 최종적으로 해당 테스트 케이스 번호와 함께 result를 10진수로 변환한 값을 출력한다.

'''
