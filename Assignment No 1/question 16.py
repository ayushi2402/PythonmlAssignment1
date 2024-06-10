s=input()
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for c in d:
    print(c,":",d[c])
