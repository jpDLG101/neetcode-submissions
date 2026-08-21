class Solution:

    def encode(self, strs: List[str]) -> str:
        print(f"len lista original {len(strs)}")
        if strs == []:
            return "##"
        c = 1
        for s in range(len(strs)):
            strs.insert(c, ";:")
            c+=2
        print(f"string original: {strs}")
        print(f"string sin la madre del final {"".join(strs[:-1])}")
        return "".join(strs[:-1])
 
    def decode(self, s: str) -> List[str]:
        if s == "##":
            return []
        print(f"len de s:{len(s)}")
        print(f"input decoder {s}")
        print(f"respuesta {list(s.split(";:"))}")
        return list(s.split(";:"))



