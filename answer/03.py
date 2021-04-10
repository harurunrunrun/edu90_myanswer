class dijkstra:
  def __init__(self,N):
    self.INF=float("inf")
    self.G=[[] for _ in [0]*(N+1)]
    self.d=[self.INF]*(N+1)
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
    que=[]
    heapify(que)
    self.d[s]=0
    heappush(que,[0,s])
    while que:
      p=heappop(que)
      v=p[1]
      if self.d[v]<p[0]:
        continue
      for i in range(len(self.G[v])):
        e=self.G[v][i]   
        if self.d[e[0]]>self.d[v]+e[1]:
          self.d[e[0]]=self.d[v]+e[1]
          heappush(que,[self.d[e[0]],e[0]])
    return self.d

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

def main():
  N=pin(1)
  d=[pin(2)for _ in [0]*(N-1)]
  G1=dijkstra(N)
  for i in d:
    G1.add2(i[0]-1,i[1]-1,1)
  d1=G1.run(0)
  num1=0
  ind=0
  for i in range(N):
    if num1<d1[i]:
      ind=i
      num1=d1[i]
  G2=dijkstra(N)
  for i in d:
    G2.add2(i[0]-1,i[1]-1,1)
  d2=G2.run(ind)
  num2=0
  for i in range(N):
    num2=max(num2,d2[i])
  print(num2+1)
  return

main()
