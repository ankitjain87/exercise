class ProducerConsumer:
    def __init__(self, capacity):
        self.start = 0
        self.counter = 0
        self.store = {}
        self.capacity = capacity

    def push(self, el):
        self.store[self.counter] = el
        self.counter += 1

        if len(self.store) > self.capacity:
            del self.store[self.start]
            self.start += 1


    def pull(self, ind):
        if ind >= self.counter:
            return None

        for j in range(ind, self.counter):
            if j in self.store and self.store[j] != None:
                x = self.store[j]
                self.store[j] = None
                return x

        return None


pc = ProducerConsumer(3)
pc.push("a")
pc.push("b")
pc.push("c")

print(pc.store)

print(pc.pull(3))
print(pc.pull(0))
print(pc.pull(1))
print(pc.pull(0))
print(pc.pull(0))

print(pc.store)

pc.push("d")
pc.push("e")
pc.push("f")
pc.push("g")
print(pc.store)

print(pc.pull(7))
print(pc.pull(3))
print(pc.pull(5))
pc.push("h")
print(pc.store)