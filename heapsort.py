''' Example of Ascending '''
import heapq

def heapsort(i):
    number = []
    result = []
    for value in i:
        heapq.heappush(number, value)
    
    for i in range(len(number)):
        result.append(heapq.heappop(number))
    
    return result

result = heapsort([0, 9, 1, 8, 3, 2, 7, 4, 6, 5])
print(result)


''' Example of Descending '''
import heapq

def heapsort(i):
    number = []
    result = []
    for value in i:
        heapq.heappush(number, -value)

    for i in range(len(number)):
        result.append(-heapq.heappop(number))

    return result

result = heapsort([0, 9, 1, 8, 3, 2, 7, 4, 6, 5])
print(result)



