from collections import deque

class Solution:
    def numIslands(self, grid):
        self.grid = grid
        self.visited = set()
        self.num_islands = 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.visited:
                    continue

                if grid[i][j] == "1":
                    self.num_islands += 1
                    self.bfs(i, j)

        return self.num_islands


    def bfs(self, i, j):
        q = deque()
        q.append((i, j))

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                self.visited.add(node)
                new_points = [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]
                for new_point in new_points:
                    if self.validate_pos(new_point[0], new_point[1]) and new_point not in self.visited and self.grid[new_point[0]][new_point[1]] == "1":
                        q.append(new_point)
                        self.visited.add(new_point)

    def validate_pos(self, i, j):
        return (i < self.rows and i >= 0 and j < self.cols and j >= 0)

