class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ññ"
        return "ñññ".join(strs)
 
    def decode(self, s: str) -> List[str]:
        if s == "ññ":
            return []
        return list(s.split("ñññ"))



