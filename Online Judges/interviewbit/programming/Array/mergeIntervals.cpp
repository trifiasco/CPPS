/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
 
 bool cmp(const Interval& a, const Interval &b)
 {
     if(a.start < b.start)
     {
         return true;
     }
     else if(a.start == b.start)
     {
         if(a.end < b.end)
            return true;
     }
     return false;
 }
 
vector<Interval> Solution::insert(vector<Interval> &intervals, Interval newInterval) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    vector<Interval> a = intervals;
    vector<Interval> res;
    if(newInterval.start > newInterval.end)
    {
        swap(newInterval.start, newInterval.end);
    }
    int flag = 0;
    for(int i =0; i < a.size(); i++)
    {
        if((newInterval.start >= a[i].start && newInterval.start <= a[i].end) || (newInterval.end >= a[i].start && newInterval.end <= a[i].end))
        {
            //this is a merge condition
            int newStart = min(a[i].start, newInterval.start);
            int newEnd = max(a[i].end, newInterval.end);
            int j;
            for(j = i+1; j < a.size(); j++)
            {
                if(newEnd >= a[j].start)
                {
                    newEnd = max(a[j].end, newEnd);
                    i = j;
                }
                else if(newEnd < a[j].start)
                {
                    i = j - 1;
                    break;
                }
            }
            flag = 1;
            res.push_back(Interval(newStart, newEnd));
        }
        else if(newInterval.start > a[i].start)
        {
            res.push_back(a[i]);
        }
        else if(newInterval.end < a[i].start)
        {
            if(!flag)
            {
                flag = 1;
                res.push_back(Interval(newInterval.start, newInterval.end));
            }
            res.push_back(a[i]);
        }
    }
    if(!flag)
        res.push_back(Interval(newInterval.start, newInterval.end));
    return res;
    
}

