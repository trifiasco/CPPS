#include <bits/stdc++.h>

using namespace std;

vector<int> Solution::maxset(vector<int> &A) {
    int size = A.size();
    long long maxLen = 0, maxSum = 0, curSum = 0, curLen = 0, startIndex = 0;
    
    for(int i = 0; i <= size; i++)
    {
        if(i == size)
        {
            if(curSum > maxSum)
            {
                maxSum = curSum;
                maxLen = curLen;
                startIndex = i - curLen;
            }
            else if(curSum == maxSum)
            {
                if(curLen > maxLen)
                {
                    maxSum = curSum;
                    maxLen = curLen;
                    startIndex = i - curLen;
                }
            }
            continue;
        }
        if(A[i] >= 0)
        {
            curSum += (long long)A[i];
            curLen += 1;
        }
        else
        {
            if(curSum > maxSum)
            {
                maxSum = curSum;
                maxLen = curLen;
                startIndex = i - curLen;
            }
            else if(curSum == maxSum)
            {
                if(curLen > maxLen)
                {
                    maxSum = curSum;
                    maxLen = curLen;
                    startIndex = i - curLen;
                }
            }
            
            curSum = 0;
            curLen = 0;
        }
    }
    
    vector <int> result;
    
    for(int i = 0, j = startIndex; i < maxLen; i++, j++)
    {
        result.push_back(A[j]);
    }
    
    return result;
}




int main()
{

  vector<int> v;
  v.push_back(1967513926);
  v.push_back(1540383426);
  v.push_back(-1303455736);
  v.push_back(-521595368);
  v.push_back(-7);
  maxset(v);
  return 0;
}
