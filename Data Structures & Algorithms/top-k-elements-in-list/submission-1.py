class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map =  {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] = hash_map[i] + 1
    
        lyst = sorted(hash_map,key=hash_map.get, reverse=True)[:k]
        return lyst