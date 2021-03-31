def main():
  N=int(input())
  if N&1:
    return
  ansl=[]
  m=pow(2,N-1)
  for i in range(pow(2,N)):
    ans=""
    a=0
    b=0
    f=False
    cnt=0
    M=m
    for j in range(N):
      if (i>>j)&1:
        ans+="("
        a+=1
      else:
        ans+=")"
        b+=1
        cnt+=M
      M//=2
      if a<b:
        f=True
        break
    if f or a!=b:
      continue
    ansl.append([cnt,ans])
  for i in sorted(ansl,key=lambda x:x[0]):
    print(i[1])
  return

main()


