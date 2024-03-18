#include <bits/stdc++.h>

using namespace std;

const int max_n = 100001;
const int max_q = 100001;

int drink[max_n] = {0,};
int max_drink[max_n];
int root[max_n];

int find(int x){
	if(x == root[x]){
		return x;
	}
	return root[x] = find(root[x]);
}
void union_(int x, int y){
	x = find(x);
	y = find(y);
	if (x >= y){
		root[y] = x;
	}
	else{
		root[x] = y;
	}
}

int main(){
	for (int i = 0; i < max_n; i++){
		root[i] = i;
	}
	cin.tie(nullptr), ios::sync_with_stdio(false);
	int n,q;
	cin >> n >> q;
	for(int i = 1; i <= n; i++){
		cin >> max_drink[i];
	}
	for(int i =0;i<q;i++){
		int a,b;
		cin >>a;
		if (a == 1){
			int c;
			cin >> b >> c;
			int pos = find(b);
			int litter = c;
			while (litter > 0 && pos <= n){
				if (max_drink[pos] - drink[pos] >= litter){
					drink[pos] += litter;
					litter = 0;
				}
				else{
					if (pos == n){
						drink[pos] = max_drink[pos];
						break;
					}
					litter -= max_drink[pos] - drink[pos];
					drink[pos] = max_drink[pos];
					union_(pos, pos+1);
					pos = root[pos];
				}
			}
		}
		else{
			cin >> b;
			cout << drink[b] << "\n";
		}
	}
	return 0;
}
