class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # b ucket sort was so easy
        # bucket should be sorted absed on frequency of elements
        # 1) have hashmap to calculate freq 
        # 2) make bucket based on freq 
        # 3) add top k elements to res
        # 1)
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        #print(hashmap)
        bucket = [[] for i in range(len(nums) + 1)]
        #print(bucket)
        for key, value in hashmap.items():
            #print(key, value)
            bucket[value].append(key)
        #print(bucket)
        res = []
        # 3) inside bucket just enter top k most elements 
        for i in range(len(bucket) - 1, 0, -1):
            tmp = bucket[i]
            if k != 0:
                for value in tmp:
                    res.append(value)
                    k -= 1
        #print(res)
        return res
