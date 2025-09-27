from src.linear_list.vec import Vec


class Queue:
    vec: Vec

    def __init__(self, capacity):
        self.size = 0
        self.vec = Vec(capacity)

    def enqueue(self, item):
        if self.vec.size == self.vec.capacity:
            raise Exception("Queue is full")
        self.vec.push(item)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self.vec[0]
        self.size -= 1
        self.vec.remove(0)
        return val

    def is_empty(self):
        return self.vec.size == 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size


