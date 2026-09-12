class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap is way better for this 
        # bucket sort code is hard but easy to solve 
        hashmap = {}
        bucket = [[] for i in range(len(nums) + 1)]
        # 1) count freq 
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        # 2) create bucket based on freq 
        for key, value in hashmap.items():
            bucket[value].append(key)
        # 3) join freq to list and return 
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for value in bucket[i]:
                res.append(value)
                if len(res) == k:
                    return res
        #print(res)