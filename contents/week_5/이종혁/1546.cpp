// boj 1546 평균 
// bronze 1

#include <iostream>
#include <vector>
#include<queue>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);


    int n, max = 0;
    float result = 0.f;
    priority_queue<int> pq;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        pq.push(num);
    }
    max = pq.top();
    
    while (!pq.empty())
    {
        result += (static_cast<float>(pq.top())/max)*100;
        pq.pop();
    }
    result /= n;
    cout << result;

    return 0;
}