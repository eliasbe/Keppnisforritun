#include <stdio.h>
#define MAXN 1000000

int p[MAXN + 1]; // = [-1, -1, ..., -1]
int find(int x) { return p[x] < 0 ? x : (p[x] = find(p[x])); }

void join(int x, int y) {
  int rx = find(x), ry = find(y);
  if (rx == ry)
    return;
  if (p[rx] > p[ry])
    p[ry] += p[rx], p[rx] = ry;
  else
    p[rx] += p[ry], p[ry] = rx;
}

int main() {
  int i, n, q;
  for (i = 0; i < MAXN; i++)
    p[i] = -1;
  scanf("%d%d\n", &n, &q);

  char staf;
  int a, b;
  for (i = 0; i < q; i++) {
    scanf("%c%d%d\n", &staf, &a, &b);
    if (staf == 't')
      join(a, b);
    if (staf == 's')
      printf("%d\n", -p[find(a)]);
  }
  return 0;
}
