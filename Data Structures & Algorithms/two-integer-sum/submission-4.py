class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, num in enumerate(nums):
            comp[target-num] = i

        for j, num in enumerate(nums):
            if num in comp and j != comp[num]:
                return [j,comp[num]]
