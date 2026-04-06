class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        best = 0
        p = 0
        while i < j:
            p = min(heights[i], heights[j]) * (j - i)
            if p > best:
                best = p
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return best


        