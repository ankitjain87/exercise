class KthLargest(object):
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap_list = [0]
        self.heap_size = 0
        self.k = k

        for i in nums:
            self.insert(i)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.insert(val)
        return self.heap_list[1]

    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

    def insert(self, el):
        if self.heap_size == self.k:
            if el < self.heap_list[1]:
                return

        self.heap_list.append(el)
        self.heap_size += 1
        self.sift_up(self.heap_size)

        if self.heap_size > self.k:
            self.delete_min()

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


k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(3, arr)
print(kthLargest.add(3))   # returns 4
print(kthLargest.add(5))   # returns 5
print(kthLargest.add(10))  # returns 5
print(kthLargest.add(9))   # returns 8
print(kthLargest.add(4))   # returns 8
