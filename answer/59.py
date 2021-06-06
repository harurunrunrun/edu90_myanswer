from sys import stdin
pin=stdin.readline
def main():
  N,M,Q=map(int,pin().split())
  G=[[]for _ in[0]*N]
  for _ in[0]*M:
    X,Y=map(int,pin().split())
    G[X-1].append(Y-1)
  d=[]
  c=1
  for _ in[0]*N:
    d.append(c)
    c<<=1
  for i in range(N):
    for j in G[i]:
      d[j]|=d[i]
  for _ in [0]*Q:
    A,B=map(int,pin().split())
    if (d[B-1]>>(A-1))&1:
      print("Yes")
    else:
      print("No")
  return
  
main()
