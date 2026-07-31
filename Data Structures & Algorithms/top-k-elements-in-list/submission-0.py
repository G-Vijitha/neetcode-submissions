import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        heap = []

        for number, count in freq.items():
            heapq.heappush(heap,(-count, number))
        
        answers= []
        for _ in range(k):
            count, number = heapq.heappop(heap)
            answers.append(number)
        return answers        