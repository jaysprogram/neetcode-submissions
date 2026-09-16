class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for i in s:
            if i not in countS:
                countS[i] = 1
            else:
                countS[i] += 1

        for i in t:
            if i not in countT:
                countT[i] = 1
            else:
                countT[i] += 1

        if len(countT) == len(countS):
            for i in countT:
                if countS.get(i) == None or (countT.get(i) != countS.get(i)):
                    return False
            return True
        return False