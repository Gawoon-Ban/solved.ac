#include <bits/stdc++.h>

using namespace std;

const int MX = 1005;

int N, M, V, visited[MX];
vector <int> adj[MX];

void DFS(int pos){
    visited[pos] = true;
    cout << pos << " ";
    for(int nxt : adj[pos]){
        if(visited[nxt]) continue;
        DFS(nxt);
    }
}

void BFS(){
    queue <int> q;
    for(int i = 1; i <= N; i++) visited[i] = 0;

    q.push(V);
    visited[V] = true;
    while(!q.empty()){
        int pos = q.front();
        cout << pos << " ";
        q.pop();
        for(int nxt : adj[pos]){
            if(visited[nxt]) continue;
            q.push(nxt);
            visited[nxt] = true;
        }
    }
    cout << "\n";
}

int main(){
    cin.tie(nullptr), ios::sync_with_stdio(false);
    cin >> N >> M >> V;

    for(int i = 0; i < M; i++){
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for(int i = 1; i <= N; i++){
        sort(adj[i].begin(), adj[i].end());
    }
    DFS(V);
    cout << "\n";
    BFS();
}