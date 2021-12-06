from hashlib import sha256

data = input()

print(sha256(data.encode()).hexdigest())


# 1. hashlib 라이브러리를 선언해 sha256을 사용할 수 있도록 한다.
# 2. 출력 시 sha256을 통해 입력값을 인코딩하여 출력한다.
