class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        mult = 1

        for i , num in enumerate(reversed(nums)):
            mult = num * mult
            postfix.insert(0, mult)

        mult = 1
        for i , num in enumerate(nums):
            mult = num * mult
            prefix.append(mult)

        res = []

        for idx in range(len(nums)):
            print(idx)
            if idx > len(nums) - 2:
                res.append(prefix[idx - 1])
            elif idx == 0:
                res.append(postfix[idx + 1])
            else:
                res.append(prefix[idx -1] * postfix[idx + 1]) 
        return res
