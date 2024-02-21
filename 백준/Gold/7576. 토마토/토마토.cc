#include <bits/stdc++.h>

using namespace std;

const int MX = 1005;

const int dr[4] = {1, -1, 0, 0};
const int dc[4] = {0, 0, 1, -1};

int R, C, arr[MX][MX];

int main(){
    cin.tie(nullptr), ios::sync_with_stdio(false);
    cin >> C >> R;

    for(int r = 1; r <= R; r++)
    for(int c = 1; c <= C; c++) cin >> arr[r][c];

    queue <pair<int, int> > q;
    for(int r = 1; r <= R; r++)
    for(int c = 1; c <= C; c++){
        if(arr[r][c] == 1) q.push({r, c});
    }

    while(!q.empty()){
        pair <int, int> pos = q.front();
        q.pop();
        int r = pos.first;
        int c = pos.second;

        for(int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];

            if(nr < 1 || nc < 1 || nr > R || nc > C) continue;
            if(arr[nr][nc] != 0) continue;

            arr[nr][nc] = arr[r][c] + 1;
            q.push({nr, nc});
        }
    }

    bool flag = true;
    int max_value = 0;
    for(int r = 1; r <= R; r++)
    for(int c = 1; c <= C; c++){
        if(arr[r][c] == 0) flag = false;
        max_value = max(max_value, arr[r][c]);
    }

    if(!flag) cout << "-1";
    else cout << max_value - 1;
}
