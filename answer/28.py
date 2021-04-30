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
  N=pin()
  l=range(1001)
  #l=range(6)
  d=[[0]*1002 for i in [0]*1002]
  #d=[[0]*6 for i in range(6)]
  for _ in [0]*N:
    lx,ly,rx,ry=pin(4)
    d[lx][ly]+=1#左下
    d[lx][ry]-=1#左上
    d[rx][ly]-=1#右下
    d[rx][ry]+=1#右上
  #print(*d,sep="\n")
  for x in l:
    for y in l:
      d[x][y]+=d[x-1][y]
  for x in l:
    for y in l:
      d[x][y]+=d[x][y-1]
  ans=[0]*(N+1)
  for x in l:
    for y in l:
      ans[d[x][y]-1]+=1
  print(*ans[:-1],sep="\n")
  #print(*d,sep="\n")
  #print(ans)
  return


main()
