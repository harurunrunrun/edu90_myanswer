from collections import*
N,*S=open(0)
d=Counter()
for i in range(int(N)):
 if d[S[i]]==0:d[S[i]]=i+1,print(i+1)