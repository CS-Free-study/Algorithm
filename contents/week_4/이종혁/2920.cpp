// boj 2920 음계
// bronze 2

#include<iostream>
#include<string>

using namespace std;

int main(int argc, char* argv[])
{
	ios_base::sync_with_stdio(false);
	string scale;

	getline(cin, scale);

	if (scale == "1 2 3 4 5 6 7 8")
		cout << "ascending";
	else if (scale == "8 7 6 5 4 3 2 1")
		cout << "descending";
	else
		cout << "mixed";


	return 0;
}