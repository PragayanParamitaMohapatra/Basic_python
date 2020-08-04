import time
def firstn(num):
    n=1
    while n <= num:
        yield n
        n=n+1
for x in firstn(10):
    print(x)
    time.sleep(5)