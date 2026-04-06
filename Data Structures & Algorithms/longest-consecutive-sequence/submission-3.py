class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in n:
                q = 1
                while num + 1 in n:
                    q += 1
                    num += 1
                best = max(q, best)

        return best




