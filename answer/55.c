N,P,Q,i,j,k,l,m;long A[105],a;main(){scanf("%d%d%d",&N,&P,&Q);for(;scanf("%d",&A[i]),i<N;i++)for(j=i;--j>2;)for(k=j;--k>1;)for(l=k;--l;)for(m=l;m;)A[i]*A[j]%P*A[k]%P*A[l]%P*A[--m]%P-Q||a++;printf("%d",a);}