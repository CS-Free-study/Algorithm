// boj 1157 단어 공부
// bronze 1

#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    // 65~90   -> % 65 
    // 97~122  -> % 97
    
    
    string word;

    cin >> word;
    int count[26] = {};
    int idx, max=0;
    char result;
    
    for (int i = 0; i < word.size(); i++)
    {
        int w = static_cast<int>(word[i]);
        if (w >= 65 && w <= 90)
        {
            count[w%65]++;
        }
        else if (w >= 97 && w <= 122)
        {
            count[w%97]++;
        }
    }
    
    for (int i = 0; i < 26; i++)
    {
        if (count[i] > max)
        {
            max = count[i];
            idx = i;
        }
            
    }
    result = idx + 65;
    for (int i = 0; i < 26; i++)
    {
        if (i == idx)
            continue;
        if (max == count[i])
            result = '?';
    }
    
    cout << result;

    return 0;
}