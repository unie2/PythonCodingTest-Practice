score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())
for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    data = []
    for _ in range(n) :
        a, b, c = map(int, input().split())
        sum_value = (a * 0.35) + (b * 0.45) + (c * 0.2)
        data.append(sum_value)

    k_score = data[k-1]
    data.sort(reverse=True)

    value = n // 10
    result = data.index(k_score) // value

    print("#%d %s" % (tc, score[result]))
    
'''
1. 각 점수에 대한 등급을 구성한 score 리스트를 정의한다.
2. 각 테스트 케이스마다 n과 k를 입력받고 총점을 담기 위한 data 리스트를 초기화한다.
3. 각 학생에 대한 세 가지 점수를 입력받아 문제에서 제시한 비율로 계산하여 세 점수를 합한 값을 data 리스트에 추가한다.
4. 구하고자 하는 학생의 점수를 k_score에 할당하고, data 리스트를 내림차순으로 정렬한다.
5. n / 10 명의 학생들에게 동일한 평점을 부여할 수 있으므로, n // 10을 계산하여 value에 할당한다.
6. 해당 점수(k_score)에 해당되는 인덱스를 찾아 value로 나눠 result에 할당하고, 최종적으로 해당 테스트 케이스 번호와 함께 등급(score[result])을 출력한다.

'''
