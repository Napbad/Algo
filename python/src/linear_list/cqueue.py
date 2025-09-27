
class cqueue:
    front: int
    rear: int
    size: int
    capacity: int

    def is_full(self):
        return (self.rear + 1 + self.capacity) % self.capacity == self.front

    def is_empty(self):
        return self.front == self.rear

    def front_add(self):
        if self.is_empty():
            raise Exception("Queue is empty")

    def rear_add(self):
        if self.is_full():
            raise Exception("Queue is full")