decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/'
      ]

t = int(input())
for i in range(1, t + 1) :
    word = list(input())
    value = ''
    for j in range(len(word)) :
        num = decode.index(word[j])
        bin_num = str(bin(num)[2:])

        while len(bin_num) < 6 :
            bin_num = '0' + bin_num
        value += bin_num

    result = ''
    for j in range(len(word)*6 // 8) :
        data = int(value[j*8 : j*8+8], 2)
        result += chr(data)

    print('#%d %s' % (i, result))
    
'''
1. 문제에서 제시한 표를 decode 리스트에 정의한다.
2. 각 테스트 케이스마다 문자열을 입력받고, decode리스트를 통해 확인하고 있는 문자를 숫자로 변환하여 num에 할당한다.
3. num을 이진수로 변환하고 이진수의 경우 '0b' 가 앞에 붙기 때문에 [2:]를 통해 '0b'를 잘라준다.
4. 이후 while문을 통해 bin_num의 길이가 6이 될때까지 앞에 '0'을 붙여주고, while문 작업이 끝나면 value에 bin_num을 추가한다.
5. 입력받은 문자열의 길이에 6을 곱하고 8 비트씩 자른 값을 반복문의 범위로 하여 자른 값을 10진수로 변환하여 data에 할당하고 data 값을 문자형으로 변환하여 result에 추가한다.
6. 이와 같은 반복 작업이 끝나면 해당 테스트 케이스 번호와 함께 result 값을 출력한다.

'''
