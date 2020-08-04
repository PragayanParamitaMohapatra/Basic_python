class Solution:
   def minDeletionSize(self, A):
      return sum([1-(sorted(col)==list(col)) for col in zip(*A)])
ob = Solution()
print(ob.minDeletionSize(["cba","daf","ghi"]))
