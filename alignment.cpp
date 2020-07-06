#include<bits/stdc++.h>

using namespace std;

string make_left_align(vector<string> words, int n)
{
  int current_line = 0;
  string result = "";
  for(int i = 0; i < words.size(); i++)
  {
    if(current_line + words[i].size() + 1 <= n)
    {
      if(current_line != 0)
      {
        result += " ";
      }
      result += words[i];
      current_line += words[i].size() + 1;
    }
    else
    {
      current_line = 0;
      result += "|\n";
    }
  }
  return result;
}

string make_right_align(vector<string> words, int n)
{
  int current_line = 0;
  string result = "";
  string temp_result = "";
  for(int i = 0; i < words.size(); i++)
  {
    if(current_line + words[i].size() + 1 <= n)
    {
      if(current_line != 0)
      {
        temp_result += " ";
      }
      temp_result += words[i];
      current_line += words[i].size() + 1;
    }
    else
    {
      int rest = n - current_line;
      //int now = ceil(rest/2.0)
      for(int j = 0; j < rest; j++)
      {
        result += " ";
      }
      result += temp_result;
      result += "|\n";
      temp_result = "";
      current_line = 0;

    }
  }
  return result;
}

int main()
{
  //int a[5] = {1,1,2,2,3};

  string sentence = "this should be a long sentence. this is another line. this should one more time.";
  stringstream ss(sentence);
  vector<string> vs;
  string word;

  while(ss >> word)
  {
    vs.push_back(word);
  }

  int allowed_character_in_one_line = 16;

  string left_aligned = make_left_align(vs, allowed_character_in_one_line);
  cout<< left_aligned << endl;

  string right_aligned = make_right_align(vs, allowed_character_in_one_line);
  cout<< right_aligned << endl;


  return 0;
}
