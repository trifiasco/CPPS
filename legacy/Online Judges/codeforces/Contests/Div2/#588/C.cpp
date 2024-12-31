#pragma comment(linker, "/stack:640000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
const double PI=acos(-1.0);

#define    READ(f) 	         freopen(f, "r", stdin)
#define    WRITE(f)   	     freopen(f, "w", stdout)
#define    MP(x, y) 	     make_pair(x, y)
#define    PB(x)             push_back(x)
#define    rep(i,n)          for(int i = 1 ; i<=(n) ; i++)
#define    repI(i,n)         for(int i = 0 ; i<(n) ; i++)
#define    FOR(i,L,R) 	     for (int i = L; i <= R; i++)
#define    ROF(i,L,R) 	     for (int i = L; i >= R; i--)
#define    FOREACH(i,t)      for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define    ALL(p) 	         p.begin(),p.end()
#define    ALLR(p) 	         p.rbegin(),p.rend()
#define    SET(p) 	         memset(p, -1, sizeof(p))
#define    CLR(p)            memset(p, 0, sizeof(p))
#define    MEM(p, v)         memset(p, v, sizeof(p))
#define    getI(a) 	         scanf("%d", &a)
#define    getII(a,b) 	     scanf("%d%d", &a, &b)
#define    getIII(a,b,c)     scanf("%d%d%d", &a, &b, &c)
#define    getL(a)           scanf("%lld",&a)
#define    getLL(a,b)        scanf("%lld%lld",&a,&b)
#define    getLLL(a,b,c)     scanf("%lld%lld%lld",&a,&b,&c)
#define    getC(n)           scanf("%c",&n)
#define    getF(n)           scanf("%lf",&n)
#define    getS(n)           scanf("%s",n)
#define    bitCheck(N,in)    ((bool)(N&(1<<(in))))
#define    bitOff(N,in)      (N&(~(1<<(in))))
#define    bitOn(N,in)       (N|(1<<(in)))
#define    iseq(a,b)          (fabs(a-b)<EPS)
#define    ff 	 first
#define    ss 	 second
#define    ll	 long long
#define    ull 	 unsigned long long


typedef pair<int,int>pii;
typedef vector<pii>vpii;
typedef vector<int>vi;
typedef vector<vi>vii;


template< class T > inline T _abs(T n) { return ((n) < 0 ? -(n) : (n)); }
template< class T > inline T _max(T a, T b) { return (!((a)<(b))?(a):(b)); }
template< class T > inline T _min(T a, T b) { return (((a)<(b))?(a):(b)); }
template< class T > inline T _swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > inline T gcd(T a, T b) { return (b) == 0 ? (a) : gcd((b), ((a) % (b))); }
template< class T > inline T lcm(T a, T b) { return ((a) / gcd((a), (b)) * (b)); }
template <typename T> string NumberToString ( T Number ) { ostringstream ss; ss << Number; return ss.str(); }

#ifdef howcum
     #define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

//// 4 direction
//int dx[]={-1,1,0,0};
//int dy[]={0,0,-1,1};
//
//// 8 direction
//int dx[]={-1,1,0,0,-1,-1,1,1};
//int dy[]={0,0,-1,1,-1,1,1,-1};
//
//// horse
//int dx[] = {-2,-2,2,2,-1,-1,1,1};
//int dy[] = {1,-1,-1,1,2,-2,-2,2};

//int n, m;

vector<vector<int>> adjlist;
vector<pair<int, int> > dominos;


vector<int>vis, marked, mp;
//map<int, pair<int, int> mp;

vector<pair<int, int> > edges;

int call(int pos, int n)
{
  cout<< pos << endl;
//  for(int i = 0; i < 21; i++)
//  {
//    cout<< marked[i] <<  " ";
//  }
//  cout<< endl;

  for(int i = 1; i <= n; i++)
  {
    cout<< mp[i] << " ";
  }
  cout<< endl;

  if(pos == n)
  {
    return 0;
  }

  int u = edges[pos].first;
  int v = edges[pos].second;

  int u_facing = mp[u];
  int v_facing = mp[v];

  int ans = 0;

  for(int i = 0; i < dominos.size(); i++)
  {
    if(marked[i])
      continue;

    pair<int, int> domino = dominos[i];
    if(domino.ff == u_facing && domino.ss == v_facing)
    {
      marked[i] = 1;
      ans = max(ans, 1 + call(pos + 1, n));
      marked[i] = 0;
    }
    else if(domino.ss == u_facing && domino.ff == v_facing && domino.ff != domino.ss)
    {
      marked[i] = 1;
      ans = max(ans, 1 + call(pos + 1, n));
      marked[i] = 0;
    }

    else if(domino.ff == u_facing)
    {
      marked[i] = 1;
      mp[v] = domino.ss;
      ans = max(ans, 1 + call(pos + 1, n));
      marked[i] = 0;
      mp[v] = -1;
    }
    else if(domino.ss == u_facing)
    {
      marked[i] = 1;
      mp[v] = domino.ff;
      ans = max(ans, 1 + call(pos + 1, n));
      marked[i] = 0;
      mp[v] = -1;
    }

    else if(domino.ff == v_facing)
    {
      marked[i] = 1;
      mp[u] = domino.ss;
      ans = max(ans, 1 + call(pos + 1, n));
      marked[i] = 0;
      mp[u] = -1;
    }
    else if(domino.ss == v_facing)
    {
      marked[i] = 1;
      mp[u] = domino.ff;
      ans = max(ans, 1 + call(pos + 1, n));
      marked[i] = 0;
      mp[u] = -1;
    }
    else
    {
      marked[i] = 1;
      mp[u] = domino.ff;
      mp[v] = domino.ss;
      ans = max(ans, 1 + call(pos + 1, n));
      if(domino.ff != domino.ss)
      {
        mp[u] = domino.ss;
        mp[v] = domino.ff;
        ans = max(ans, 1 + call(pos + 1, n));
      }
      mp[u] = -1;
      mp[v] = -1;
    }

  }
  ans = max(ans, call(pos + 1, n));

  return ans;
}

int main() {
READ("in.txt");
    #ifdef howcum
        READ("in.txt");
        //WRITE("out.txt");
    #endif // howcum
//    ios_base::sync_with_stdio(0); cin.tie(0);


    int cnt = 0;
    for(int i = 1; i <= 6; i++)
    {
      for(int j = i; j <= 6; j++)
      {
        cnt++;
        dominos.push_back(make_pair(i, j));
        //cout<< i << " " << j << endl;
      }
    }

    //cout<< cnt << endl;


    int n,m;
    while(cin>>n>>m)
    {
      adjlist.assign(n + 1, vi());

      for(int i = 0; i < m; i++)
      {
        int u, v;
        cin>> u >> v;

        edges.push_back(make_pair(u, v));

        adjlist[u].push_back(v);
        adjlist[v].push_back(u);
      }
      vis.assign(n + 1, 0);
      marked.assign(21, 0);
      mp.assign(n + 1, -1);
      for(int i = 1; i <= n; i++)
  {
    cout<< mp[i] << " ";
  }
  cout<< endl;
      int res = call(0, m);
      cout<< res << endl;
      //return 0;
    }

    return 0;
}




