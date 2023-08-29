import heapq

def get_max(lst):
    heap = []
    original = []
    for i in lst:
        heapq.heappush(heap, -i)
    max_value = -1*heapq.heappop(heap)
    for i in heap:
        original.append(-i)
    heapq.heapify(original)
    return original, max_value

def solution(operations):
    answer = []
    heap = []
    for oper in operations:
        o = oper.split(" ")
        value = int(o[1])
        if o[0] == 'I':
            heapq.heappush(heap, value)
        if o[0] == 'D':
            if o[1] == '1' and len(heap) > 0:
                heap, max_value = get_max(heap)
            elif o[1] == '-1' and len(heap) > 0:
                heapq.heappop(heap)

    if len(heap) == 0 : return [0,0]
    answer = [max(heap), min(heap)]
    return answer
