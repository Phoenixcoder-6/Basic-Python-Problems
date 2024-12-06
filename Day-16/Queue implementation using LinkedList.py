class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0  # Initialize size to track the number of elements in the queue

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            # If the queue is empty, both front and rear point to the new node
            self.front = self.rear = new_node
        else:
            # Link the new node to the end of the queue
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1  # Increment the size after adding an element

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        # Store the data of the front node
        temp = self.front.data
        # Move the front pointer to the next node
        self.front = self.front.next
        # If the queue becomes empty, set rear to None as well
        if self.front is None:
            self.rear = None
        self.size -= 1  # Decrement the size after removing an element
        return temp

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.data

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Nothing to show.")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Print None after the queue elements

# Example Usage
q1 = Queue()

# Enqueue elements
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

# Display the queue
q1.display()

# Peek at the front element
print(f"Front element: {q1.peek()}")

# Dequeue elements
q1.dequeue()
q1.dequeue()

# Display the queue
q1.display()

# Check size
print(f"Queue size: {q1.get_size()}")
