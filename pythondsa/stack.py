class Stack:
    def __init__(self):
        self.stack = []

    # Method to add an element to the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    # Method to remove the top element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack.pop()

    # Method to return the top element without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack[-1]

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to print the stack
    def print_stack(self):
        print("Stack:", self.stack)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()  # Output: Stack: [1, 2, 3]

    print("Top element is:", stack.peek())  # Output: Top element is: 3

    print("Popped element is:", stack.pop())  # Output: Popped element is: 3
    stack.print_stack()  # Output: Stack: [1, 2]

    print("Is the stack empty?", stack.is_empty())  # Output: Is the stack empty? False

    stack.pop()
    stack.pop()
    print("Popped element is:", stack.pop())  # Output: Popped element is: Stack is empty.
