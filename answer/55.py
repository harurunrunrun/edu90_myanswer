import itertools as t
N,P,Q,*A=map(int,open(0).read().split())
print(sum(1for a,b,c,d,e in t.combinations(A,5)if a*b%P*c%P*d%P*e%P==Q))