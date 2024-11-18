import heapq
def merge_k_sorted_array(lists):
    heap=[]
    for i,lst in enumerate(lists):
        if lst:
            heapq.heappush(heap,(lst[0],i,0))

    result=[]

    while heap:
        value,list_index,ele_index=heapq.heappop(heap)
        result.append(value)

        if ele_index+1<len(lists[list_index]):
            next_value= lists[list_index][ele_index+1]
            heapq.heappush(heap,(next_value,list_index,ele_index+1))
    return result


lists=[[1,4,5],[2,3,6],[4,7]]
res= merge_k_sorted_array(lists)
print(res)