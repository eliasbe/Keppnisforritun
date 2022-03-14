// The classic knapsack problem

#include <assert.h>
#include <stdio.h>
#define MAXN 2001 // Mesti fjöldi hluta
#define MAXC 2001 // Mesta rýmd
#define INF (1 << 30)

int max(int a, int b) {
  if (a > b)
    return a;
  return b;
}

int d[MAXN][MAXC], a[MAXN], b[MAXN];
int dp_lookup(int x, int y) {
  // x er númer hlutar, y er rýmdin sem eftir er
  // a er virði hlutar og b er þyngd
  if (y < 0) // Neikvæð rýmd, ólögleg staða
    return -INF;
  if (x < 0) // út fyrir fylkið
    return 0;
  if (d[x][y] != -1)
    return d[x][y];
  return d[x][y] = max(dp_lookup(x - 1, y), dp_lookup(x - 1, y - b[x]) + a[x]);
  // Annað hvort tökum við hlutin, minnkum rýmd og hækkum gildi eða þá sleppum
  // honum
}

void knapsack(int *v, int *w, int *r, int n, int c) {
  int i, j, s[MAXN], ss;
  // Upphafsstilling
  for (i = 0; i < n; i++)
    for (j = 0; j <= c; j++)
      d[i][j] = -1;
  for (i = 0; i < n; i++)
    a[i] = v[i], b[i] = w[i], r[i] = 0;
  j = c;
  for (i = n - 1; i >= 0; i--)
    if (dp_lookup(i - 1, j) < dp_lookup(i - 1, j - w[i]) + v[i])
      j -= w[i], r[i] = 1; // teljum hvaða hlutir eru teknir með
}

int main() {
  int k, n, c, i, j, v[MAXN], w[MAXN], r[MAXN];
  while (scanf("%d%d", &c, &n) != EOF) {
    for (i = 0; i < n; i++)
      scanf("%d%d", &v[i], &w[i]);
    knapsack(v, w, r, n, c);
    for (k = i = 0; i < n; i++)
      k += r[i];
    printf("%d\n", k); // Hversu margir hlutir
    for (i = 0; i < n; i++)
      if (r[i])
        printf("%d ", i); // Hvaða hlutir
    printf("\n");
  }
  return 0;
}
