

int dfs(int x, int y, int a, int b, vector< vector<int> > &vis)
{
    if(x == a && y == b)
    {
        return 0;
    }
   vis[x][y] = 1;
   
   int dx[]={-1,1,0,0,-1,-1,1,1};
   int dy[]={0,0,-1,1,-1,1,1,-1};
   
   int res = 0;
   
   for(int i = 0; i < 8; i ++)
   {
       int tx = x + dx[i];
       int ty = y + dy[i];
       
       if(vis[tx][ty] == 0)
       {
           res = min(res, 1 + dfs(tx, ty, a, b, vis));
       }
   }
   
   return res;
}

int Solution::coverPoints(vector<int> &A, vector<int> &B) {
    
    int nowx = A[0];
    int nowy = B[0];
    //return 0;
    
/// if it needs to converted into positive values only
    /*int mn = 0;
    
    for(int i = 0; i < A.size(); i++)
    {
        mn = min(mn, A[i]);
        mn = min(mn, B[i]);
    }
    
    if(mn < 0)
    {
        mn = mn * -1;
        for(int i = 0; i < A.size(); i++)
        {
            A[i] += mn;
            B[i] += mn;            
        }

    }*/
    
    int nextx , nexty;
    int res = 0;
    for(int i = 1; i < A.size(); i++)
    {
        nextx = A[i];
        nexty = B[i];
        
        //vector < vector < int> > vis (A.size(), vector<int>(A.size(), 0));
        
        //res += dfs(nowx, nowy, nextx, nexty, vis);
        res += max(abs(nowx-nextx), abs(nowy-nexty));
        nowx = nextx;
        nowy = nexty;
        
    }
    
    return res;
    
}

