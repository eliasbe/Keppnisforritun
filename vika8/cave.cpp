#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
vi low, num;
int curnum;

void dfs(vvi &g, vi &cp, vii &bri, int u, int p) {
  low[u] = num[u] = curnum++;
  int cnt = 0;
  bool found = false;
  for (int v : g[u]) {
    if (num[v] == -1) {
      dfs(g, cp, bri, v, u);
      low[u] = min(low[u], low[v]);
      cnt++;
      found |= low[v] >= num[u];
      if (low[v] > num[u])
        bri.push_back(ii(u, v));
    } else if (p != v)
      low[u] = min(low[u], num[v]);
  }
  if (found && (p != -1 || cnt > 1))
    cp.push_back(u);
}
pair<vi, vii> cutpointsbridges(vvi &g) {
  vi cp;
  vii bri;
  num = vi(g.size(), -1);
  low.resize(g.size());
  curnum = 0;
  for (int i = 0; i < g.size(); ++i) {
    if (num[i] == -1) {
      dfs(g, cp, bri, i, -1);
    }
  }
  return pair<vi, vii>(cp, bri);
}
