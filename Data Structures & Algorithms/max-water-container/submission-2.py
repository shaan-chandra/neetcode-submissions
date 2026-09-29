class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            area = 0
            min_height = min(heights[left], heights[right])
            #print("min height: ", min_height)
            area = min_height * (right - left)
            #print("area we got: ", area)
            res = max(area, res)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        #print(res)
        return res