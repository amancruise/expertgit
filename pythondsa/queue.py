class Queue:
    def __init__(self):
        self.queue = []

    # Method to add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    # Method to remove the front element from the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty."
        return self.queue.pop(0)

    # Method to return the front element without removing it
    def front(self):
        if self.is_empty():
            return "Queue is empty."
        return self.queue[0]

    # Method to check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Method to print the queue
    def print_queue(self):
        print("Queue:", self.queue)

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()  # Output: Queue: [1, 2, 3]

    print("Front element is:", queue.front())  # Output: Front element is: 1

    print("Dequeued element is:", queue.dequeue())  # Output: Dequeued element is: 1
    queue.print_queue()  # Output: Queue: [2, 3]

    print("Is the queue empty?", queue.is_empty())  # Output: Is the queue empty? False

    queue.dequeue()
    queue.dequeue()
    print("Dequeued element is:", queue.dequeue())  # Output: Dequeued element is: Queue is empty.
