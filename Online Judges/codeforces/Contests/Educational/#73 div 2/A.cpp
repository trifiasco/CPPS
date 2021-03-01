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

vector<int> a;

int call(int pos, int now, int n)
{
  if(pos == n)
  {
    return now == 2048;
  }

  if(now == 2048)
  {
    return 1;
  }

  int ans = 0;

  if(a[pos] == now)
  {
    a[pos] = 0;
    ans = ans || call(pos + 1, now * 2, n);
    a[pos] = now;
  }

  ans = ans || call(pos + 1, now, n);

  return ans;

}

int main() {
    //READ("in.txt");
    #ifdef howcum
        READ("in.txt");
        //WRITE("out.txt");
    #endif // howcum
//    ios_base::sync_with_stdio(0); cin.tie(0);


    int n;

    vector<int> relevant;
    int power = 1;
    relevant.push_back(power);
    for(int i = 0; ; i++)
    {
      power *= 2;
      //cout<< i << " " << pow(2, i) << endl;
      relevant.push_back(power);
      if(power >= 2048)
        break;
    }

//    for(int i = 0; i < relevant.size();i++)
//    {
//      cout<< relevant[i] << " ";
//    }

    int q;
    cin>>q;
    while(q--)
    {
      cin>>n;

      //vector<int> a;
      map<int, int> mp;
      int inp;

      int flag = 0;

      for(int i = 0; i < n; i++)
      {
        cin>>inp;
        if(inp <= 2048)
        {
          a.push_back(inp);
          mp[inp]++;
          if(inp == 2048)
          {
            flag = 1;
          }
        }
      }

      if(flag)
      {
        cout<< "YES" << endl;
        continue;
      }


      sort(a.begin(), a.end());

      //cout<< call(1, a[0], n) <<  endl;

      for(int i = 0; i < relevant.size() - 1; i++)
      {
        int now = relevant[i];

        int nowCount = mp[now];

        int full = nowCount / 2;

        int rem = nowCount % 2;

        mp[now * 2] += full;
        mp[now] = rem;
      }

      if(mp[2048] > 0)
      {
        cout<< "YES" << endl;
      }
      else
      {
        cout<< "NO" << endl;
      }

    }

    return 0;
}




