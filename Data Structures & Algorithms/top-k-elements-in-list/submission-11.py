class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force would be to sort the array
        hashmap = {}
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        tmp = []
        for key, value in hashmap.items():
            tmp.append([value,key])
        #print(sorted(tmp, reverse = True))
        tmp = sorted(tmp, reverse = True)
        res = []
        counter = 0
        while k != 0:
            #print(tmp[counter][1])
            res.append(tmp[counter][1])
            counter += 1
            k -= 1
        #print(res)
        return res


            