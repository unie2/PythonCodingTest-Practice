data = input()

for i in range(len(data)) :
    print(ord(data[i])-64, end=' ')
    
# 1. 입력받은 문자열의 길이만큼 반복 수행하고, 각 알파벳을 아스키코드 값으로 변환한 후 64를 뺀 값을 출력한다.
