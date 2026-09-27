class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        l = 0
        currBest = 0

        for r in s:
            while r in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(r)
            if len(seen) > best:
                best = len(seen)
        return best