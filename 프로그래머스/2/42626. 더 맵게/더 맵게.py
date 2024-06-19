import heapq

def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    return answer
