t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
 
for tc in range(1, t + 1) :
    n = int(input())
    index = 0
     
    result = [0] * 8
    while n >= 10 :
        if money[index] <= n :
            result[index] += n // money[index]
            n %= money[index]
        else :
            index += 1
    print('#%d' % tc)
    for i in range(8) :
        print(result[i], end=' ')
    print()
    
'''
1. 문제에서 제시한 화폐의 종류를 구성하여 money 리스트에 정의한다.
2. 각 테스트 케이스마다 index를 0으로 초기화하고 각 화폐가 사용된 개수를 0으로 초기화한 result 리스트를 정의한다.
3. n이 1의 자리가 될 때까지 반복 수행하며, money[index]가 n보다 작거나 같을 경우에는 아래와 같이 수행한다.
  - result[index]에 n을 money[index]로 나눈 값을 더한다.
  - n을 money[index]로 나눈 나머지 값으로 갱신한다.
4. money[index]가 n보다 클 경우 단순히 index를 1 증가시켜 다음 화폐로 확인할 수 있도록 한다.
5. 반복 작업이 종료되면 해당 테스트 케이스 번호와 함께 result 리스트 요소들을 하나씩 출력한다.

'''
