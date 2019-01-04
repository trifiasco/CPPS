int next_bigger(vector<int> &v, int i, stack<int>& s)
{
    while(!s.empty())
    {
        int j = s.top();
        if(v[j] <= v[i])
        {
            s.pop();
        }
        else
        {
            s.push(i);
            return j;
        }
    }
    s.push(i);
    return 0;
}

int Solution::maxSpecialProduct(vector<int> &A) {
    
    vector<int> left, right;
    left.assign(A.size()+1, 0);
    right.assign(A.size()+1, 0);
    
    stack<int> ss1,ss2;
    
    for(int i = 0; i < A.size(); i++)
    {
        left[i] = next_bigger(A, i, ss1);
    }
    for(int i = A.size()-1; i >= 0; i--)
    {
        right[i] = next_bigger(A, i, ss2);
    }
    long long maxi = 0;
    for(int i = 0, j = A.size()-1; i < A.size(); i++, j--)
    {
        long long temp = ((((long long)left[i]) % 1000000007) * (((long long)right[i]) % 1000000007)) % 1000000007;
        maxi = max(maxi, temp);
    }
    
    return ((int)maxi);
}

