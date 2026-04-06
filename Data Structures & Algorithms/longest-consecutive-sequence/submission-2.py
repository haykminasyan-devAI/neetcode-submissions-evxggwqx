class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p = sorted(nums)
        q = 1
        best = 1
        for i in range(1,len(p)):
            if p[i] == p[i-1]:
                continue
            if p[i] - p[i-1] == 1:
                q += 1
            else:
                q = 1
            
            best = max(best, q)

        return best


