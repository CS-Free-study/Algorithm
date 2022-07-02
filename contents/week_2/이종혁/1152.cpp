// boj 1152 단어의 개수
// bronze 2

#include<iostream>
#include<string>


using namespace std;


int main(int argc, char * argv[])
{
	ios_base::sync_with_stdio(false);
	string word;
	int count = 0;
	getline(cin, word);
	for (int i = 0; i < word.length(); i++)
	{
		if (word[i] == ' ')
			count++;
	}
	if (word[0] == ' ')
		count--;
	if (word[word.length()-1] == ' ')
		count--;
	cout << ++count;
	return 0;
}