class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]
        print(self.hashmap[key])

    def get(self, key: str, timestamp: int) -> str:
        retrieve_results = self.hashmap.get(key)
        if retrieve_results is None:
            return ""
        left = 0
        right = len(retrieve_results)
        while left < right:
            mid = (left + right) // 2
            if retrieve_results[mid][1] <= timestamp:
                left = mid + 1
            elif retrieve_results[mid][1] > timestamp:
                right = mid 
        if left == 0:
            return ""
        elif left > 0:
            return retrieve_results[left - 1][0]
