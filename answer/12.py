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

from networkx.utils import UnionFind
from collections import Counter
def main():
  H,W=pin(2)
  Q=pin(1)
  uf=UnionFind()
  C=Counter()
  for _ in [0]*Q:
    t=pin(1)
    if t==1:
      x,y=pin(2)
      x-=1
      y-=1
      C[(x,y)]=1
      for i in [(0,1),(0,-1),(1,0),(-1,0)]:
        if C[(x+i[0],y+i[1])]==1:
          uf.union((x,y),((x+i[0],y+i[1])))
    else:
      xa,ya,xb,yb=pin(4)
      if C[(xa-1,ya-1)]==0:
        print("No")
      elif uf[(xa-1,ya-1)]==uf[(xb-1,yb-1)]:
        print("Yes")
      else:
        print("No")
  return

main()
