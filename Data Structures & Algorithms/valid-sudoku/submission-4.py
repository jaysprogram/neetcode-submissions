class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to check all directions in a grid
        directions = [[0, 1], [0, 0], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        # check all the rows
        for row in range(9):
            seen = set()
            for num in board[row]:
                if not num.isdigit():
                    continue
                num = int(num)

                if num in seen:
                    return False
                else:
                    seen.add(num)

        # check 3 x 3 squares
        for row in [1, 4, 7]:
            for col in [1, 4, 7]:
                seen = set()
                for x,y in directions:
                    r = row + x
                    c = col + y

                    num = board[r][c]
                    if not num.isdigit():
                        continue

                    num = int(num)
                    if num in seen:
                        return False
                    else:
                        seen.add(num)


        # check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]

                if not num.isdigit():
                    continue
                
                if int(num) in seen:
                    return False
                else:
                    seen.add(int(num))



        return True
