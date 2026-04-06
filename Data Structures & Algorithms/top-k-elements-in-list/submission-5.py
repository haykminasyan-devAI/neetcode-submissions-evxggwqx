class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        b = [[] for _ in range(len(nums) + 1)]

        for num , fr in counts.items():
            b[fr].append(num)


        res = []

        for i in reversed(b):
            if len(i) > 0:
                for n in i:
                    res.append(n)
                    if len(res) == k:
                        return res
            


        
        