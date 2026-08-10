class TimeMap:
    # Brute force: O(n)
    #optimal(binary) - set: O(1), get: O(logn), space:O(n)

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        left = 0
        right = len(values)-1
        ans = ""
        while left <= right:
            mid = left + (right - left)//2
            stored_time, stored_value = values[mid]
            if stored_time <= timestamp:
                ans = stored_value
                left = mid + 1
            else:
                right = mid - 1
        return ans

        # print("range(len(values)-1, -1, -1)",range(len(values)-1, -1, -1))
        # for i in range(len(values)-1, -1, -1):
        #     # print("i:", i)
        #     stored_time, stored_value = values[i]
        #     if stored_time <= timestamp:
        #         return stored_value
        # return ""
        
