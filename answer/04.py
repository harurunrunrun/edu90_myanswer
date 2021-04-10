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
  H,W=pin(2)
  A=[pin(W,int,True)for _ in [0]*H]
  tate=[0]*W
  yoko=[0]*H
  for i in range(H):
    for j in range(W):
      tate[j]+=A[i][j]
      yoko[i]+=A[i][j]
  for i in range(H):
    ans=[]
    for j in range(W):
      ans.append(yoko[i]+tate[j]-A[i][j])
    print(*ans)
  return

main()
