#include <bits/stdc++.h>
using namespace std;

int main() {
  ifstream fin("data/gen1.out");
  if (!fin.is_open()) return 0;

  int prev = -1;
  int cnt = 0;
  string s;
  vector<int> v;

  char c;
  while (fin.get(c)) {
    if (c == prev) {
      cnt++;
    } else {
      if (cnt > 0) {
        s += char(prev);
        v.push_back(cnt);
      }
      prev = c;
      cnt = 1;
    }
  }

  if (cnt > 0) {
    s += char(prev);
    v.push_back(cnt);
  }

  cout << "string s1 = \"" << s << "\";\n";
  cout << "vector<int> v1 = {";
  for (int x : v) cout << x << ",";
  cout << "};\n";
}