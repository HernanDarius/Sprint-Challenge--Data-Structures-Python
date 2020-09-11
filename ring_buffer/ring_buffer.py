class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.current] = item  
            self.current = self.current+1 if self.current+1 < len(self.data) else 0
        else:
            self.data.append(item)

    def get(self):
        return self.data