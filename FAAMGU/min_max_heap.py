# 0, 5, 3, 7, 8, 1, 6, 9, 4
# 0  1  2  3  4  5  6  7  8


    #           5
    #     10         4
    #  15    21   38    20



class MinHeap():

    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, el):
        self.heap_list.append(el)
        self.heap_size += 1
        self.sift_up(self.heap_size)

    def get_min_child(self, i):
        if 2*i + 1 > self.heap_size:
            return 2*i # left child

        if self.heap_list[i*2] < self.heap_list[i*2 + 1]:
            return 2*i # left child

        return 2*i + 1 # right child


    def sift_down(self, i):
        while (i * 2) <= self.heap_size:
            min_child_index = self.get_min_child(i)
            if self.heap_list[i] > self.heap_list[min_child_index]:
                self.heap_list[i], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[i]
            i = min_child_index

    def delete_min(self):
        if len(self.heap_list) == 1:
            return None

        if self.heap_size == 1:
            return self.heap_list.pop()

        min_val = self.heap_list[1]

        self.heap_list[1] = self.heap_list.pop()
        self.heap_size -= 1

        self.sift_down(1)
        return min_val


class MaxHeap():
    
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, el):
        self.heap_list.append(el)
        self.heap_size += 1
        self.sift_up(self.heap_size)

    def get_max_child(self, i):
        if 2*i + 1 > self.heap_size:
            return 2*i # left child

        if self.heap_list[i*2] > self.heap_list[i*2 + 1]:
            return 2*i # left child

        return 2*i + 1 # right child


    def sift_down(self, i):
        while (i * 2) <= self.heap_size:
            max_child_index = self.get_max_child(i)
            if self.heap_list[i] < self.heap_list[max_child_index]:
                self.heap_list[i], self.heap_list[max_child_index] = self.heap_list[max_child_index], self.heap_list[i]
            i = max_child_index

    def delete_max(self):
        if len(self.heap_list) == 1:
            return None

        if self.heap_size == 1:
            return self.heap_list.pop()

        max_val = self.heap_list[1]

        self.heap_list[1] = self.heap_list.pop()
        self.heap_size -= 1

        self.sift_down(1)
        return max_val

my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print("Min heap", )
for i in range(8):
    print(my_heap.delete_min(), end=" ")

print()

my_heap = MaxHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print("Max heap => ")
for i in range(7):
    print(my_heap.delete_max(), end=" ")
