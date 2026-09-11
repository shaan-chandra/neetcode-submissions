class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1, hashmap2 = {}, {}
        for s1 in s:
            hashmap1[s1] = hashmap1.get(s1, 0) + 1
        for s2 in t:
            hashmap2[s2] = hashmap2.get(s2, 0) + 1
        print("map1: ", hashmap1, "map2: ", hashmap2)
        return hashmap1 == hashmap2