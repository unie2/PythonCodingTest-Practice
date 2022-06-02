def solution(k, dungeons) :
    return search(k, dungeons, 0)


def search(k, dungeons, cnt) :
    cnt_list = [cnt]

    for i in range(len(dungeons)) :
        if dungeons[i][0] <= k :
            temp_list = dungeons.copy()
            del temp_list[i]
            cnt_list.append(search(k - dungeons[i][1], temp_list, cnt + 1))

    
    return max(cnt_list)
  
'''
1. search() 함수의 작업은 아래와 같다.
  - cnt_list에 전달받은 cnt 값을 리스트 형태로 하여 정의한다.
  - dungeons 요소를 하나씩 확인하면서, 만약 현재 최소 필요 피로도가 k보다 작거나 같다면 temp_list에 dungeons 리스트를 복사한다.
  - 이후 temp_list의 현재 인덱스 값(i)을 삭제하고 search() 함수를 재귀 호출하여 반환받은 값을 cnt_list에 추가한다.
  - cnt_list 리스트에 존재하는 값 중 최대값을 반환한다.
  - 즉, 던전에 들어갈 때마다 피로도를 감소시키고, 현재 들어간 던전을 제외한 리스트를 다시 search() 함수에 전달하여 가장 많이 들어간 값(cnt)을 반환한다.

'''
