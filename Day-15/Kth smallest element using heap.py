import heapq
def kth_element(arr,k):
    max_heap=[]
    for num in arr:
        heapq.heappush(max_heap,-num)

        if len(max_heap)>k:
            heapq.heappop(max_heap)

    return -max_heap[0]

arr=[2,1,5,47,3,8]
k=4
res= kth_element(arr,k)
print(res)

