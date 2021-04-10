#解説AC
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
  N,L,K=pin(3)
  A=pin(0)
  ac=0
  wa=L+1
  ans=0
  for _ in [0]*40:
    M=(ac+wa)//2
    cnt=0
    S=0
    a=float("inf")
    #db=[]
    for i in A:
      s=i
      if s-S>=M:
        cnt+=1
        a=min(a,s-S)
        #db.append(s-S)
        S=s
        s=0
    if L-S>=M:
      cnt+=1
      a=min(a,L-S)
      #db.append(L-S)
    #print(ans,cnt,ac,wa)
    if cnt>=K+1:
      ac=M
      ans=max(ans,a)
    else:
      wa=M
    #print(ans,db)
    
  print(ans)
  return

main()
