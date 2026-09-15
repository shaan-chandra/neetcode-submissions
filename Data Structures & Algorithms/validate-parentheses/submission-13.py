class Solution:
    def isValid(self, s: str) -> bool:
        # first come with brute force
        # understand and state problem correctly 
        # just code three rules 
        # easy 
        # but how do I code even brute force 
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            print(s == "")
        return s == ""