import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        # Use a heap with negative frequency and word
        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)
        
        # Pop top k elements
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result