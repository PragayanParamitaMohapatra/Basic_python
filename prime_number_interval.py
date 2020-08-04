def main(n1,n2):
    for val in range(n1,n2 + 1):
      if val > 1:
        for n in range(2, val//2 + 2):
            if (val % n) == 0:
                break
            else:
                if n == val//2 + 1:
                   print(val)
n1=int(input("num1:"))
n2=int(input("num2:"))
main(n1,n2)
