#include<bits/stdc++.h>

using namespace std;


void basic()
{
  int a[5] = {1,1,2,2,3};

  map<int, int> mp;

  for(int i = 0; i < 5; i++)
  {
    //int current = a[i];
    mp[a[i]]++;
  }

  for(int i = 1; i <= 100; i++)
  {
    if(mp[i])
    {
      cout<< i << ": " << mp[i]<< endl;
    }
  }
}

//node - parent
//1    - null
//2    - 1
//3    - 1
//4    - 2

struct node{
  int val;
  int parent;
};

void call(vector<node> nodes)
{
  int len = nodes.size();

  map<int, DS> mp;

  for(int i = 0; i < nodes.size(); i++)
  {
    node current_node = nodes[i];
    if(current_node.parent == 0)
    {
      // ekhane new ekta DS init korte hobe.
      mp[current_node.val] = DS;
    }
    else
    {
      DS jekhane_insert_korbo = mp[current_node.parent];
      jekhane_insert_korbo.push(node);
    }
  }

}

int main()
{

  //basic();

  vector<node> vs;

  for(int i = 1; i <= 5; i++)
  {
    node temp;
    temp.val = i;
    temp.parent = i / 2;
    vs.push_back(temp);
  }

  for(int i = 0; i < 5; i++)
  {
    cout<< vs[i].val << " " << vs[i].parent << endl;
  }

  return 0;
}

