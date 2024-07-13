import heapq

# Creating a max-heap
max_heap = []

# Insertion (Push)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -30)

# To print the heap in a more understandable way, we negate the values back
print("Max-Heap after insertion:", [-x for x in max_heap])  # Output: Max-Heap after insertion: [30, 20, 5, 10]

# Peek (getting the largest element)
print("Peek (largest element):", -max_heap[0])  # Output: Peek (largest element): 30

# Deletion (Pop)
largest = -heapq.heappop(max_heap)
print("Popped element:", largest)  # Output: Popped element: 30
print("Max-Heap after popping:", [-x for x in max_heap])  # Output: Max-Heap after popping: [20, 10, 5]
