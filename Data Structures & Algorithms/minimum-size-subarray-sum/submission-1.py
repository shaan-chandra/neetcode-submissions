class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        ans , curr = float("inf"), 0
        for right in range(len(nums)):
            curr += nums[right]
            while (curr >= target):
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1
        print(ans)
        if ans == float("inf"):
            return 0
        return ans