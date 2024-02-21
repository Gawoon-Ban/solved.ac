#include <bits/stdc++.h>

using namespace std;

const int MX = 2000;
const int MX2 = 2000;

int N, K, W[MX], V[MX], dp[MX][MX2], penalty;

int main(){
    cin.tie(nullptr), ios::sync_with_stdio(false);
    cin >> N >> K;
    for(int i = 1; i <= N; i++)
    {
        cin >> W[i]  >> V[i];
        penalty = penalty + V[i];
    }
    for(int n = 1; n <= N; n++){
        for(int k = 0; k <= K; k++){
            dp[n][k] = dp[n - 1][k];
            if(k - W[n] >= 0) dp[n][k] = max(dp[n][k], dp[n - 1][k - W[n]] + V[n]);
        }
    }

    cout << penalty - dp[N][K];
}