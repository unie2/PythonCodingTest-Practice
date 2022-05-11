t = int(input())
 
for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    data.sort()
    sum_value = sum(data[1:9])
    avg_value = round(sum_value / 8)
     
    print('#%d %d' % (tc, avg_value))
    
    
'''
1. 각 테스트 케이스마다 10개의 수를 입력받고, 최댓값과 최솟값을 제외하기 위해 오름차순으로 정렬한다.
2. 정렬된 data 리스트 내 요소 중 가장 첫번째 요소와 마지막 요소를 제외한 나머지 요소들의 합을 구해 sum_value에 할당한다.
3. round() 를 통해 sum_value를 8로 나눈 값을 반올림한 정수 값으로 변환한다.
4. 최종적으로 해당 테스트 케이스 번호와 함께 평균값(avg_value)을 출력한다.

'''
