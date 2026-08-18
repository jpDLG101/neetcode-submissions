class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fst = list(s)
        sec = list(t)
        return sorted(fst) == sorted(sec)