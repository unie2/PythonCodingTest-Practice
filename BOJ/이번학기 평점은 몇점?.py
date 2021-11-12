diction = {"A+":4.3, "A0":4.0, "A-":3.7, "B+":3.3, "B0":3.0, "B-":2.7,
	"C+":2.3, "C0":2.0, "C-":1.7, "D+":1.3, "D0":1.0, "D-":0.7, "F":0.0}

t = int(input())

count = 0
result = 0
for _ in range(t) :
  a, b, c = input().split()
  b = int(b)
  result += b * diction[c]
  count += b

print("%.2f" % (round(result/count + 10**-10, 2)))


# 1. 문제에서 제시되어 있는 성적을 딕셔너리로 구성한다.
# 2. 입력받은 각 과목의 학점(b) * 성적(diction[c])을 result에 계속해서 누적해간다.
# 3. 총 학점을 의미하는 count에 각 과목의 학점(b)를 누적한다.
# 4. 최종적으로 출력 시 round( )를 이용하여 result / count를 계산하여 소수점 둘째 자리까지 출력한다.
