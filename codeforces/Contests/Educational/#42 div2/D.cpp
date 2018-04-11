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


typedef pair<ll,ll>pii;
typedef vector<pii>vpii;
typedef vector<ll>vi;
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


int main() {
    #ifdef howcum
        READ("in.txt");
        //WRITE("out.txt");
    #endif // howcum
//    ios_base::sync_with_stdio(0); cin.tie(0);

    int n;
    while(cin >> n)
    {
        ll a[n+1];
        priority_queue < pii > pq;
        for( int i = 0; i < n; i++)
        {
            cin >> a[i];
            pq.push(pii(-a[i], -i));
        }

        vi res;
        res.assign(n+1, -1);
        int cnt = 0;
        while(!pq.empty())
        {
            pii first = pq.top();
            pq.pop();
            if(pq.empty())
            {
                cnt+=1;
                res[first.ss*(-1)] = first.ff * (-1);
                break;
            }
            pii second = pq.top();
            pq.pop();
            if(first.ff == second.ff)
            {
                ll newEntry = first.ff*2LL;
                ll pos = second.ss;
                pq.push(pii(newEntry, pos));
            }
            else
            {
                cnt+=1;
                res[first.ss*(-1)] = first.ff * (-1);
                pq.push(second);
            }
        }

        cout<< cnt << endl;

        for(int i = 0; i < n; i++)
        {
            if(res[i] != -1)
            {
                cout<< res[i] << " ";
            }
        }
        cout<< endl;




    }
    return 0;
}




