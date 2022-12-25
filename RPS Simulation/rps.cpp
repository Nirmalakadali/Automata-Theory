#include <bits/stdc++.h>
using namespace std;

int main()
{
    char arr[1000];
    int A[1000][1000];

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> arr[i];
        for (int j = 1; j <= 3; j++)
        {
            cin >> A[i][j];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        if (arr[i] == 'R')
        {
            A[i][1] = A[i][2];
        }
        else if (arr[i] == 'P')
        {
            A[i][2] = A[i][3];
        }
        else
        {
            A[i][3] = A[i][1];
        }
    }
    for (int i = 1; i <= n; i++)
    {
        if (arr[i] == 'R')
        {
            arr[i] = 'P';
        }
        else if (arr[i] == 'P')
        {
            arr[i] = 'S';
        }
        else
        {
            arr[i] = 'R';
        }
    }
    cout << n << endl;
    for (int i = 1; i <= n; i++)
    {
        cout << arr[i] << " ";
        for (int j = 1; j <= 3; j++)
        {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}