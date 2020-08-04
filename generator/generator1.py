g=(x*x for x in range(10))#generator automatic call tuple comphrension
while True:
    print(next(g))



# Advantage of generators:
# ------------------------
# **** Performance will be improved
# ****Memory utilisation will be improved
# ****when compared with normal iterators generators are easy to use
# ***generators best suitable for web scraping