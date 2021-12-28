import itertools
import math

def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w + n for w in weak]
    minCnt = math.inf # 무한대 값
    for start in range(weakSize) :
        for d in itertools.permutations(dist, len(dist)) :
            cnt = 1
            pos = start
            for i in range(1, weakSize) :
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt-1] : # 도달하지 못할 경우
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist) :
                        break
            if cnt <= len(dist) :
                minCnt = min(minCnt, cnt) # 최솟값 갱신
    if minCnt == math.inf :
        return -1
    
    return minCnt
