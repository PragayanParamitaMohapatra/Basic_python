# freq=lambda n:n*f(n-1) if n>0 else 1
# print(freq(7))

txt = "hello"
d = dict(map(lambda x : (x, txt.count(x)), set(txt)))
print(d)