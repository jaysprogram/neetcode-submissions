class Solution:

    def encode(self, strs: List[str]) -> str:
        newstring = ""
        for i in strs:
            newstring += i + "é"

        return newstring

    def decode(self, s: str) -> List[str]:
        res = s.split("é")
        del res[-1]
        return res
