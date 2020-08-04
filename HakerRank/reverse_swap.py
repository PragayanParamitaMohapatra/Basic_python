def rev_sentence(sen):
    b=sen.split(' ')
    c=''.join(reversed(b))

    return c
if __name__=="__main__":
    input="Guddi is a good girl"
    print(rev_sentence(input.swapcase()))