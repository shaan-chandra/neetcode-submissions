class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          # yea i remember keep list [] of character as key (converted to tuple as python doesnt accept list)
        # 1) iterate through nums 
        # 2) make list of the character 
        # 3) appendres(tuple(count)).append(string)
        hashmap = defaultdict(list)
        for item in strs:
            count = [0] * 26
            #print(item)
            for x in item:
                count[ord(x) - ord('a')] += 1
                #print(x)
            hashmap[tuple(count)].append(item)
        #print(hashmap.values())
        return list(hashmap.values())
