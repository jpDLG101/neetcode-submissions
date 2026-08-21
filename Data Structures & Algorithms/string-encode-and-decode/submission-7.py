class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ññ"
        c = 1
        for s in range(len(strs)):
            strs.insert(c, "ñññ")
            c+=2
        return "".join(strs[:-1])
 
    def decode(self, s: str) -> List[str]:
        if s == "ññ":
            return []
        return list(s.split("ñññ"))



