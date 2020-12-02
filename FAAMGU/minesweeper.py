"""
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]
"""
class Solution:
    def updateBoard(self, board, click):
        if not board:
            return board

        i, j = click[0], click[1]
        if board[i][j] == "M":
            board[i][j] == "X"
            return board

        self.dfs(board, i, j)
        return board


    def dfs(self, board, i, j):
        if board[i][j] != "E":
            return

        m, n = len(board), len(board[0])
        mine_count = 0
        neighbours = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

        for item in neighbours:
            new_i, new_j = i + item[0], j + item[1]
            if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] == "M":
                mine_count += 1

        print(i, j, mine_count)
        if mine_count == 0:
            board[i][j] = "B"
        else:
            board[i][j] = str(mine_count)
            return

        for item in neighbours:
            new_i, new_j = i + item[0], j + item[1]
            if 0 <= new_i < m and 0 <= new_j < n:
                self.dfs(board, new_i, new_j)



s = Solution()
board = [['E', 'E', 'E', 'E', 'E'],
['E', 'E', 'M', 'E', 'E'],
['E', 'E', 'E', 'E', 'E'],
['E', 'E', 'E', 'E', 'E']]

print(s.updateBoard(board,  [3, 0]))

