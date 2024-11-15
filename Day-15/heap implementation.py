import heapq
data=[10,20,43,1,2,65,17,44,2,3,1]
heapq.heapify(data)

print("The created heap is:",end="")
print(data)


#Pushing element 4 into heap

heapq.heappush(data,4)
print("The modified heap after push is:",end="")
print(data)

#poping element 17 from the heap

heapq.heappop(data)
print("The modified heap is:",end="")
print(data)