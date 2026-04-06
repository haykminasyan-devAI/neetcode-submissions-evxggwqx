class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
    
  
        sorted_items = sorted(count, key=lambda x: count[x], reverse=True)
    
        return sorted_items[:k]
        