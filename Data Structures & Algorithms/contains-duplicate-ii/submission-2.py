class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, hashset = 0, set()
        for index_r, value_r in enumerate(nums):
            if index_r - left > k:
                hashset.remove(nums[left])
                left += 1
            if value_r in hashset:
                return True
            hashset.add(value_r)
        return False