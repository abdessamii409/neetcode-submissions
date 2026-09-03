class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        from collections import Counter
        d1=Counter(s)
        d2=Counter(t)
        for l in d1:
            if d1[l]!=d2[l]:
                return False
        return True