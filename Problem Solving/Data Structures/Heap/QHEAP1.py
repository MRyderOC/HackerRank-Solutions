import heapq

h = []
deleted_set = set()

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        heapq.heappush(h, query[1])
    elif query[0] == 2:
        deleted_set.add(query[1])
    elif query[0] == 3:
        while h[0] in deleted_set:
            heapq.heappop(h)
        print(h[0])
