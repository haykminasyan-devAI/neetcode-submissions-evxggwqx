class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}§{s}" for s in strs)

    def decode(self, s: str) -> List[str]: 
        i = 0
        q = []
        while i < len(s):
            j = s.index("§", i)
            l = int(s[i:j])
            q.append(s[j+1 : j+1+l])
            i = j + 1 + l
        return q

