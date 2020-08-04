def print_format(num):
    w=len(str(bin(num))[2:])
    for i in range(1,num+1):
        print(str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))
if __name__=="__main__":
    n=int(input("Input num:"))
    print_format(n)
