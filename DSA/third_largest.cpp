#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    int n, q;
    cin >> n;
    if (!(n > 0 && n <= 20))
    {
        cout << "Invalid array size";
    }
    else if (n < 3)
    {
        cout << "Not sufficient elements";
    }
    else
    {
        vector<int> v;
        set<int, greater<int>> v1;
        for (int i = 0; i < n; i++)
        {
            cin >> q;
            v1.insert(q);
        }
        set<int, greater<int>>::iterator i;
        for (i = v1.begin(); i != v1.end(); i++)
        {
            v.push_back(*i);
        }
        sort(v.begin(), v.end());
        cout << v[2];
    }
    return 0;
}