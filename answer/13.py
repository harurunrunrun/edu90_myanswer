class INPUT:
  def __init__(self):
    self.l=open(0).read().split()[::-1]
    self.length=len(self.l)
    return

  def stream(self,k=1,f=int,f2=False):
    assert(-1<k)
    m=self.length
    if m==0 or m<k:
      raise Exception("There is no input!")
    elif f!=str:
      if k==0:
        self.length=0
        return list(map(f,self.l[::-1]))
      if k==1 and not f2:
        self.length-=1
        return f(self.l.pop())
      if k==1 and f2:
        self.length-=1
        return [f(self.l.pop())]
      ret=[]
      for _ in [0]*k:
        ret.append(f(self.l.pop()))
      self.length-=k
      return ret
    else:
      if k==0:
        self.length=0
        return self.l[::-1]
      if k==1 and not f2:
        self.length-=1
        return self.l.pop()
      if k==1 and f2:
        self.length-=1
        return [self.l.pop()]
      ret=[]
      for _ in [0]*k:
        ret.append(self.l.pop())
      self.length-=k
      return ret
pin=INPUT().stream

"""
pin(number[default:1],f[default:int],f2[default:False])
if number==0 -> return left all
listを変数で受け取るとき、必ずlistをTrueにすること。
"""
  
class dijkstra:
  def __init__(self,V):
    self.INF=float("inf")
    self.G=[[] for _ in [0]*V]
    self.V=V
    return
  
  def add1(self,s,t,v):
    self.G[s].append([t,v])
    return
  
  def add2(self,s,t,v):
    self.G[s].append([t,v])
    self.G[t].append([s,v])
    return

  def run(self,s):
    from heapq import heapify,heappop,heappush
    ret=[self.INF]*self.V
    que=[]
    heapify(que)
    ret[s]=0
    heappush(que,[0,s])
    while que:
      p=heappop(que)
      v=p[1]
      if ret[v]<p[0]:
        continue
      for i in range(len(self.G[v])):
        e=self.G[v][i]   
        if ret[e[0]]>ret[v]+e[1]:
          ret[e[0]]=ret[v]+e[1]
          heappush(que,[ret[e[0]],e[0]])
    return ret

def main():
  N,M=pin(2)
  ijk=dijkstra(N)
  for _ in[0]*M:
    A,B,C=pin(3)
    ijk.add2(A-1,B-1,C)
  a=ijk.run(0)
  b=ijk.run(N-1)
  for i in range(N):
    print(a[i]+b[i])
  return

main()
