class Sol:
    def numSpecial(self,A):
        codes=set()
        for word in A:
            code=''.join(sorted(word[::2]))+''.join(sorted(word[1::2]))
            codes.add(code)
        return len(codes)
ob=Sol()
print(ob.numSpecial(["aabc","abcd","abcc","xyzz","zzxy","zzyx"]))
