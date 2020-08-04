class Solution:
   def surfaceArea(self, grid):
      def adjacentArea(row):
         area = 0
         for i in range(len(row) - 1):
            if row[i] and row[i + 1]:
               area += 2 * min(row[i], row[i+1])
            return area
      z = sum([sum(i > 0 for i in row) for row in grid]) * 2
      x_plus_y = sum([sum(row) for row in grid]) * 4
      x_adjacent = sum([adjacentArea(row) for row in grid])
      y_adjacent = sum([adjacentArea(row) for row in zip(*grid)])
      return z + (x_plus_y - x_adjacent - y_adjacent)
ob = Solution()
print(ob.surfaceArea([[1,2],[3,4]]))