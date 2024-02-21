#include <bits/stdc++.h>

using namespace std;

int main(){
    cin.tie(nullptr), ios::sync_with_stdio(false);
    int N;
    cin >> N;
    for (int i=0 ; i<N;++i){
        string s;
        cin >> s;
        list <char> l;
        auto pos = l.begin();
        for(char c : s){
            if(c == '<'){
                if(pos != l.begin()) {
                    pos--;
                }
            }
            else if(c == '>'){
                if(pos != l.end()) {
                    pos++;
                }
            }
            else if(c == '-'){
                if(pos != l.begin()) {
                    pos = l.erase(--pos);
                }
            }
            else{
                pos = l.insert(pos, c);
                ++pos;
            }
        }
        for(char c : l){
            cout << c;
        }
        cout << "\n";
    }
}