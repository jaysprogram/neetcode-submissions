class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # treat it as a 1d array
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = (rows) * (cols) - 1 # m * n
        mid = (l + r) // 2

        while l <= r:
            currMid = matrix[mid // cols][mid % cols]
            if currMid  == target:
                return True
            elif currMid < target:
                l = mid + 1
                mid = (l + r) // 2
            elif currMid > target:
                r = mid - 1
                mid = (l + r) // 2

        return False

        