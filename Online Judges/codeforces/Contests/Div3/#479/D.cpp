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

ll a[110];
int n;
int marked[110];
int dir[110][110];

//int call(int pos, int cnt)
//{
//    if(cnt == n)
//    {
//        return 1;
//    }
//
//    int w1;
//    if(a[pos] % 3 == 0)
//    {
//        ll now = a[pos] / 3;
//        for(int i = 0; i < n; i++)
//        {
//            if(a[i] == now && marked[i] == 0)
//            {
//                w1 =
//            }
//        }
//    }
//
//}

int main() {
    #ifdef howcum
        READ("in.txt");
        //WRITE("out.txt");
    #endif // howcum
//    ios_base::sync_with_stdio(0); cin.tie(0);


    while(cin >> n)
    {
        for(int i = 0; i < n; i++)
        {
            cin>>a[i];
        }

        vpii pairs;
        for(int i = 0; i < n; i++)
        {
            for(int j = i+1; j < n; j++)
            {
                if(a[i] > a[j])
                {
                    if(a[i] % 3 == 0 &&  a[i] / 3 == a[j])
                    {
                        pairs.PB(pii(a[i], a[j]));
                    }
                    else if(a[i] % 2 == 0 &&  a[i] / 2 == a[j])
                    {
                        pairs.PB(pii(a[j], a[i]));
                    }
                }
                else
                {
                    if(a[j] % 3 == 0 && a[j] / 3 == a[i])
                    {
                        pairs.PB(pii(a[j], a[i]));
                    }
                    else if(a[j] % 2 == 0 && a[j] / 2 == a[i])
                    {
                        pairs.PB(pii(a[i], a[j]));
                    }
                }
            }
        }
        int cnt = 0;
        vi res;
        CLR(marked);
        sort(ALL(pairs));
        for(int i = 0 ; i < pairs.size(); i++)
            {
                debug(pairs[i].ff, pairs[i].ss);

            }
        //return 0;
        while(cnt < n )
        {
            debug(cnt);
            if(cnt == 0)
            {
                res.PB(pairs[0].ff);
                res.PB(pairs[0].ss);
                marked[0] = 1;
                cnt += 2;
                //cnt++;
                continue;
            }
            //debug(cnt)
            for(int i = 0 ; i < pairs.size(); i++)
            {
                //debug(pairs[i].ff, pairs[i].ss);
                if(res[cnt-1] == pairs[i].ff && marked[i] == 0)
                {
                    //res.PB(pairs[i].ff);
                    res.PB(pairs[i].ss);
                    marked[i] = 1;
                    cnt += 1;
                    break;
                }
                else if(res[0] == pairs[i].ss && marked[i] == 0)
                {
                    res.insert(res.begin(), pairs[i].ff);
                    marked[i] = 1;
                    cnt += 1;
                    break;
                }
            }
        }

        for(int i = 0; i < n; i++)
        {
            cout << res[i] << " ";
        }
        cout<< endl;


    }

    return 0;
}




