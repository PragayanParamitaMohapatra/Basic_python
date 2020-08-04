class Solution(object):
   def projectionArea(self, grid):
      xy = 0
      yz = 0
      xz = 0
      for r, row in enumerate(grid):
         yz += max(row)
         for c, col in enumerate(row):
            if grid[r][c] > 0:
               xy += 1
            for col in zip(*grid):
               xz += max(col)
      return xy + yz + xz
ob = Solution()
print(ob.projectionArea([[1,2],[3,4]]))