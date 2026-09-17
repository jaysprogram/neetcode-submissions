class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs =  defaultdict()

        for i in nums:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            bucket[freq].append(num)
        

        res = []
        for buck in range(len(bucket) - 1 ,0 , -1):
            for num in bucket[buck]:
                res.append(num)
                if len(res) == k:
                    return res
