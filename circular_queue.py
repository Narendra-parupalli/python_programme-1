class que_circle:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.queue = {}
        self.front = 0
        self.rear = 0

    def queue_add(self, item):
        if self.size == self.max_size:
            # Remove the oldest element
            del self.queue[self.front]
            # Move front to the next position
            self.front = (self.front + 1) % self.max_size
        else:
            self.size += 1

        # Add the new item at the rear
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size


    def display_queue(self):
        # Display the elements in the queue
        print("Circular Queue:", end=" ")
        for i in range(self.size):
            index = (self.front + i) % self.max_size
            print(self.queue.get(index, None), end=" ")
        print()

max_length = 5
circular_queue = que_circle(max_length)

for i in range(6):
    circular_queue.queue_add(f"Item {i + 1}")
    circular_queue.display_queue()
