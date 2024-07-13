import heapq

# Creating a heap
heap = []

# Insertion (Push)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 30)

print("Heap after insertion:", heap)  # Output: Heap after insertion: [5, 20, 10, 30]

# Peek (getting the smallest element)
print("Peek (smallest element):", heap[0])  # Output: Peek (smallest element): 5

# Deletion (Pop)
smallest = heapq.heappop(heap)
print("Popped element:", smallest)  # Output: Popped element: 5
print("Heap after popping:", heap)  # Output: Heap after popping: [10, 20, 30]

# Converting a list to a heap
lst = [9, 4, 7, 1, 3, 8, 5]
heapq.heapify(lst)
print("List converted to heap:", lst)  # Output: List converted to heap: [1, 3, 5, 4, 9, 8, 7]
