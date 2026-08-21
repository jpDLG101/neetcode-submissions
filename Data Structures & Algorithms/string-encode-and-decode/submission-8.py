class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ññ"
        c = 1
        l = len(strs)
        for s in range(l):
            strs.insert(c, "ñññ")
            c+=2
        return "".join(strs[:-1])
 
    def decode(self, s: str) -> List[str]:
        if s == "ññ":
            return []
        return list(s.split("ñññ"))



