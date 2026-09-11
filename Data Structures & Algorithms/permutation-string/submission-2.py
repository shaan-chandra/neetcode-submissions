class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        hashmap1, hashmap2 = {}, {}
        for item in range(len(s1)):
            hashmap1[s1[item]] = hashmap1.get(s1[item], 0) + 1
        print(hashmap1, hashmap2)
        left = 0
        k = len(s1)
        for right in range(len(s2)):
            hashmap2[s2[right]] = hashmap2.get(s2[right], 0) + 1
            if right - left + 1 > k:
                hashmap2[s2[left]] -= 1
                if hashmap2[s2[left]] == 0:
                    del hashmap2[s2[left]]
                left += 1
            if right - left + 1 == k and hashmap1 == hashmap2:
                return True
        return False

        