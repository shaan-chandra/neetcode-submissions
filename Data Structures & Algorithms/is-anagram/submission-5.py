class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cna i not just run two pointers on both strings and chcek 
        # regardless of order makes it hashmap
        hashmap1, hashmap2 = {}, {}
        for i in s:
            hashmap1[i] = hashmap1.get(i,0) + 1
        for x in t:
            hashmap2[x] = hashmap2.get(x,0) + 1
        return hashmap1 == hashmap2