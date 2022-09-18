# https://www.acmicpc.net/problem/1003

def fibo(num) :
    length = len(zero)

    if num >= length :
        for i in range(length, num + 1) :
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[num], one[num])

t = int(input())
zero = [1, 0, 1] # 0일때 1개, 1일때 0개, 2일때 1개
one = [0, 1, 1] # 0일때 0개, 1일때 1개, 2일때 1개

for _ in range(t) :
    fibo(int(input()))
    

'''
1. 입력받은 num의 zero 사용 개수는 zero[i-1] + zero[i-2]와 같다.
  0일때 : 1개
  1일때 : 0개
  2일때 : 1개
  3일때 : 1개

2. 마찬가지로 num의 one 사용 개수는 one[i-1] + one[i-2]와 같다.
  0일때 : 0개
  1일때 : 1개
  2일때 : 1개
  3일때 : 2개
 
3. 따라서 구하고자 하는 대상(num)이 현재의 zero 개수보다 클 경우 length부터 num까지 각 zero의 개수, one의 개수를 구하여 각 리스트에 추가한다.

4. 최종적으로 num을 대상으로 사용한 zero의 개수, one의 개수를 출력한다.

'''
