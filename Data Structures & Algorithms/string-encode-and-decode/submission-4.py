class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "##"
        c = 1
        for s in range(len(strs)):
            strs.insert(c, ";:")
            c+=2
        return "".join(strs[:-1])
 
    def decode(self, s: str) -> List[str]:
        if s == "##":
            return []
        return list(s.split(";:"))



