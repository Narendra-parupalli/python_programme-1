class que_circle:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.queue = {}
        self.front = 0
        self.rear = 0

    def queue_add(self, item):
        queue_depth=0
        if self.size == self.max_size:
            del self.queue[self.max_size-1]
            self.queue[self.max_size - 1] = item
            queue_depth=1

        if queue_depth==0:
            # Add the new item to the queue
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1

    def display_queue(self):
        # Display the elements in the queue
        print("Circular Queue:", end=" ")
        for i in range(self.size):
            print(self.queue.get(i, None), end=" ")
        print()

max_length = 5
circular_queue = que_circle(max_length)

for i in range(6):
    circular_queue.queue_add(f"Item {i + 1}")
    circular_queue.display_queue()