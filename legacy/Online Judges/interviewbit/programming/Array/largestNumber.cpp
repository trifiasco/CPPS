bool cmp2(const int &a, const int &b)
{
    string ab = to_string(a) + to_string(b);
    string ba = to_string(b) + to_string(a);
    return ab > ba;
}
string Solution::largestNumber(const vector<int> &A) {
    vector<int> aa;
    aa = A;
    sort(aa.begin(), aa.end(), cmp2);
    ostringstream oss;
    string a = "";
    for(int i = 0; i < aa.size(); i++)
    {
        a+= to_string(aa[i]);
    }
    if(a[0] == '0')
        return "0";
    return a;
}
