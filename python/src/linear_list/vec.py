from typing import List, Any

class Vec:

    vals: List[Any]
    size: int
    capacity: int

    MAX_CAPACITY = 1024

    def __init__(self, capacity):
        self.capacity =  capacity
        self.size = 0
        self.vals = [None] * capacity

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        return self.vals[index]

    def __setitem__(self, index, value):
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        self.vals[index] = value

    def push(self, item):
        if self.size == self.capacity:
            self.resize()

        self.vals[self.size] = item
        self.size += 1

    def resize(self):
        if self.capacity >= self.MAX_CAPACITY:
            raise MemoryError("Max capacity reached")
        self.vals = self.vals + [None] * self.capacity
        self.capacity = self.capacity * 2


    def pop(self):
        if self.size == 0:
            raise IndexError("Vector is empty")

        val = self.vals[self.size - 1]
        self.size -= 1
        return val

    def insert(self, idx, item):
        if idx < 0:
            raise IndexError("Index out of range")

        if self.size == self.capacity:
            self.resize()

        if idx > self.size:
            self.vals[self.size] = item
            self.size += 1
            return

        if idx < self.size:
            for i in range(self.size, idx, -1):
                self.vals[i] = self.vals[i - 1]
            self.vals[idx] = item
            self.size += 1
            return

    def remove(self, idx):
        if idx > self.size or idx < 0:
            return

        for i in range(idx, self.size - 1):
            self.vals[i] = self.vals[i + 1]
        self.size -= 1
        return