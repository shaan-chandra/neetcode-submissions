class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        # key:value- [ch] : [string of words ]
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            tmp = strs[i]
            ch = [0] * 26
            for c in range(len(tmp)):
                #print(tmp[c])
                #print(c)
                ch[ord(tmp[c]) - ord('a')] += 1
            #print(ch)
            hashmap[tuple(ch)].append(tmp)
        #print(hashmap)
        for i in hashmap.values():
            res.append(i)
        #print(res)
        return res
                