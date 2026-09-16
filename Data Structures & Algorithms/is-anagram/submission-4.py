class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen= len(t)
        thash = {}
        shash = {}
        s,t = list(s), list(t)

        if slen != tlen: return False

        for tc in t:
            if tc in thash:
                thash[tc] += 1
            else:
                thash[tc] = 1

        for sc in s:
            if sc in shash:
                shash[sc] +=1
            else:
                shash[sc] = 1
        
        for key in thash:
            if key in shash and shash[key] == thash[key]:
                print(key)
            else:
                return False
        return True


