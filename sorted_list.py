input("Enter values:")
a, b, c = map(int, input().split())
if a > b:
 if b > c:
   ans = [a, b, c]
elif c > a:
   ans = [c, a, b]
else:
  ans = [a, c, b]
# else:
#  if a > c:
#     ans = [b, a, c]
# elif c > b:
#    ans = [c, b, a]
# else:
# ans = [b, c, a]
print("smallest number is", ans[2])
print("next highest number is", ans[1])
print("highest number is", ans[0])



