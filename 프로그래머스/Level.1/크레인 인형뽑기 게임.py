def solution(board, moves):
    answer = 0
    case = [0]
    for i in range(len(moves)) :
        for j in range(len(board)) :
            if board[j][moves[i]-1] != 0 :
                case.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                if case[-1] == case[-2] :
                    answer += 2
                    case.pop(-1)
                    case.pop(-1)
                break
                
    return answer
  
  
'''
1. moves의 요소를 i로 활용하고, board의 요소를 j로 활용한다.
2. 만약 board[j][moves[i]-1] 값 (특정 행의 moves 특정 요소 번째 값)이 0이 아닐 경우 case에 해당 값을 추가하고 board에서는 0으로 갱신한다.
3. 그 후 조건문을 통해 바구니(case)에 방금 들어간 값이 바로 이전에 들어간 값과 일치할 경우 answer를 2 증가시키고 두 값을 빼준다.
4. 하나의 인형을 처리할 때마다 다음 moves 요소를 확인하기 위해 break 한다.
5. 위와 같은 방식으로 반복 수행을 모두 진행하고, 끝나면 answer 값을 반환한다.

'''
