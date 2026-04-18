class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num) # need to reverse numbers for a max_heap
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            pop_num = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, pop_num)
        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                pop_num = - heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, pop_num)
            else:
                pop_num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -pop_num)


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            left = -self.max_heap[0]
            right = self.min_heap[0]
            median = (left + right) / 2
            return median
        else:
            if len(self.max_heap) > len(self.min_heap):
                return - self.max_heap[0]
            else:
                return self.min_heap[0]