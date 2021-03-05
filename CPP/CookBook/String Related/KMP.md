# KMP

Text = "seventy seven"
Pattern = "seven"

### Idea

The basic idea is to pre-process the pattern. Make an lps[];

```
lps = longest proper prefix that's also a proper suffix.

lps[i] = the longest prefix in Pattern[0 - (i-1)], that's also a suffix.
```

**Proper Prefix - prefix where the whole string is not allowed**

### How to calculate LPS array:

consider the string, Pattern = "AABAA".

we need to have to track the length of longest prefix that's also a suffix.

```
lps[0] = 0; // because of the proper prefix thing.

len = 0; // initially longest proper prefix which is also a suffix is 0.
```

```
for index = 1 to string_length - 1
  if(pattern[index] == pattern[len])
  {
      //we have a match
      len++; // increase length of matched prefix
      lps[index] = len; // set lps value
      index++; // go to next index
  }
  else
  {
      //no match.

      if(index != 0)
      {
          //go backwards based on lps
          len = lps[len - 1]
          //why?? we don't have a proper prefix of length len anymore. check if there's a prefix less that len.
      }
      else
      {
          // we came at the beginning.
          lps[index] = 0;
          index++;
      }
  }

```

### Searching

Text = "AABAAC"
Pattern = "AAC"
lps[] = {0, 1, 0}

```
//initialize iterators
text_iterator = 0;
pattern_iterator = 0;

while(text_iterator < text_length)
{
    if(pattern[pattern_iterator] == text[text_iteraotr])
    {
        //we have a match. great!!
        pattern_iterator++;
        text_iterator++;
    }
    if(pattern_iterator == pattern_length)
    {
        //we found a match.
        //reset pattern_iterator
        pattern_iterator = lps[pattern_iterator - 1]
    }
    else
    {
        if(pattern_iterator != 0)
        {
            pattern_iterator = lps[pattern_iterator - 1]
        }
        else
        {
            // came to the beginning of pattern
            //need to go forward in text
            text_iterator++;
        }
    }
}

```
