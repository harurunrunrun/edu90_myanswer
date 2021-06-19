class INPUT:
  def __init__(self):
    self._l=open(0).read().split()
    self._length=len(self._l)
    self._index=0
    return

  def stream(self,k=1,f=int,f2=False):
    assert(-1<k)
    if self._length==self._index or self._length-self._index<k:
      raise Exception("There is no input!")
    elif f!=str:
      if k==0:
        ret=list(map(f,self._l[self._index:]))
        self._index=self._length
        return ret
      if k==1 and not f2:
        ret=f(self._l[self._index])
        self._index+=1
        return ret
      if k==1 and f2:
        ret=[f(self._l[self._index])]
        self._index+=1
        return ret
      ret=[]
      for _ in [0]*k:
        ret.append(f(self._l[self._index]))
        self._index+=1
      return ret
    else:
      if k==0:
        ret=list(self._l[self._index:])
        self._index=self._length
        return ret
      if k==1 and not f2:
        ret=self._l[self._index]
        self._index+=1
        return ret
      if k==1 and f2:
        ret=[self._l[self._index]]
        self._index+=1
        return ret
      ret=[]
      for _ in [0]*k:
        ret.append(self._l[self._index])
        self._index+=1
      return ret
pin=INPUT().stream

"""
pin(number[default:1],f[default:int],f2[default:False])
if number==0 -> return left all
listを変数で受け取るとき、必ずlistをTrueにすること。
"""

def main():
  N=pin(1)
  X=[]
  Y=[]
  for _ in[0]*N:
    x,y=pin(2)
    X.append(x)
    Y.append(y)
  X.sort()
  Y.sort()
  ac=-10**9-10
  wa=10**9+10
  #3分探索
  ansx=float("inf")
  searchX=lambda c:sum(abs(c-i)for i in X)
  for _ in[0]*100:
    #print(ac,wa)
    midx1=(2*ac+wa)//3
    midx2=(ac+2*wa)//3
    d1=searchX(midx1)
    d2=searchX(midx2)
    if d1<d2:
      wa=midx2
    else:
      ac=midx1
  ansx=ac
  if searchX(ac)>searchX(wa):
    ansx=wa
  if searchX(wa)>searchX((ac+wa)//2):
    ansx=(wa+ac)//2
  #print(ansx)
  ac=-10**9-10
  wa=10**+10
  searchY=lambda c:sum(abs(c-i)for i in Y)
  for _ in[0]*100:
    #print(ac,wa)
    midy1=(2*ac+wa)//3
    midy2=(ac+2*wa)//3
    d1=searchY(midy1)
    d2=searchY(midy2)
    if d1<d2:
      wa=midy2
    else:
      ac=midy1
  ansy=ac
  if searchY(ac)>searchY(wa):
    ansy=wa
  if searchY(wa)>searchY((ac+wa)//2):
    ansy=(wa+ac)//2
  #print(ansy)
  print(searchX(ansx)+searchY(ansy))
  return

main()

  