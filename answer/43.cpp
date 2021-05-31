#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

typedef struct edge{
	long long to;
	long long cost;
}Edge;
typedef pair<long,long> P;

long long INF=1000000000000000000;
int V;
vector<Edge> G[2000000];
long long d[2000000];

void dijkstra(int s){
  priority_queue<P,vector<P>,greater<P>> que;
	fill(d,d+V,INF);
	d[s]=0;
	que.push(P(0,s));
	while(!que.empty()){
		P p=que.top();que.pop();
		int v=p.second;
		if(d[v]<p.first)continue;
		for(unsigned int i=0;i<G[v].size();i++){
		  Edge e=G[v][i];
			if(d[e.to]>d[v]+e.cost){
			  d[e.to]=d[v]+e.cost;
				que.push(P(d[e.to],e.to));
			}
		}
	}
}


void G_push(int st,int to,int w){
  G[st].push_back({to,w});
  G[to].push_back({st,w});
  return;
}

int main(){
  int H,W,sx,sy,gx,gy,N;
  cin>>H>>W>>sx>>sy>>gx>>gy;
  sx--;sy--;gx--;gy--;
  N=W*H;
  V=2*N;
  vector<string> C(H);
  for(int i=0;i<H;i++)cin>>C.at(i);
  for(int i=0;i<H;i++)for(int j=0;j<W;j++){
    if(C.at(i).at(j)=='#')continue;
    if(i>0 && C.at(i-1).at(j)=='.')G_push(W*i+j,W*(i-1)+j,0);
    if(j>0 && C.at(i).at(j-1)=='.')G_push(W*i+j+N,W*i+j-1+N,0);
    G_push(W*i+j,W*i+j+N,1);
  }
  G_push(W*sx+sy,W*sx+sy+N,0);
  dijkstra(W*sx+sy);
  printf("%lld\n",min(d[W*gx+gy],d[W*gx+gy+N]));
  return 0;
}
