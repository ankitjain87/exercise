
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num):
        print("----15----", num)
        heapq.heappush(self.max_heap, num)
        heapq._heapify_max(self.max_heap)
        print("====17====", self.max_heap, self.min_heap)
        heapq.heappush(self.min_heap, self.max_heap.pop())
        heapq.heapify(self.min_heap)
        
        # print("----20-----", self.max_heap, self.min_heap)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap))
            heapq._heapify_max(self.max_heap)
            heapq.heapify(self.min_heap)
        print("----25----", self.max_heap, self.min_heap)
        

    def findMedian(self):
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] + self.max_heap[-1])/2
        
        return self.max_heap[-1]
        

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
