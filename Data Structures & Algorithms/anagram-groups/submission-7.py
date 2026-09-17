class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            str_sort = sorted(str)
            str_sort = "".join(str_sort)
            if str_sort in res:
                res[str_sort].append(str)
            else:
                res[str_sort].append(str)
        
        return list(res.values())