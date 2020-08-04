def main(n):

   if n <= 1:
    return n
   else:
    return(main(n-1) + main(n-2))
nterms = int(input("enter terms:"))
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(main(i),end="")

