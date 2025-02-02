class Queue:
    def __init__(self, initial_size=10):
        self.size = initial_size  # Initial size of the queue
        self.queue = [None] * self.size  # Initialize the queue with None values
        self.front = 0  # Index of the front element
        self.rear = -1  # Index of the rear element
        self.count = 0  # Number of elements in the queue

    def _resize(self):
        # Double the size of the queue when it's full
        new_size = self.size * 2
        new_queue = [None] * new_size

        # Copy elements from the old queue to the new queue
        for i in range(self.count):
            new_queue[i] = self.queue[(self.front + i) % self.size]

        # Update the queue and indices
        self.queue = new_queue
        self.size = new_size
        self.front = 0
        self.rear = self.count - 1

    def enqueue(self, item):
        # Resize the queue if it's full
        if self.count == self.size:
            self._resize()

        # Add the item to the rear of the queue
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        # Remove and return the front item
        item = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        # Return the front item without removing it
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0

    def __len__(self):
        return self.count

    def __str__(self):
        # Display the queue as a list (for debugging)
        return str([self.queue[(self.front + i) % self.size] for i in range(self.count)])
    

