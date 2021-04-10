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
  d=[pin(3)for _ in[0]*N]
  ans=0
  for i in range(pow(2,N)):
    s=[]
    a=0
    for j in range(N):
      if (i>>j)&1:
        a+=d[j][2]
        s.append([d[j][0]-d[j][1]+1,d[j][0]])
        #始まり、終わり
    s=sorted(s,key=lambda x:x[1])
    f=True
    e=0
    for j in range(len(s)):
      e+=s[j][1]-s[j][0]+1
      if e>s[j][1]:
        f=False
        break
    # for j in range(len(s)-1):
    #   if s[j][1]>=s[j+1][0]:
    #     f=False
    #     break
    #print(a,f,bin(i))
    if f:
      ans=max(ans,a)
    # elif a==1744196082:
    #   print(e,bin(i))
    #   print(s)
  print(ans)
  return

main()
