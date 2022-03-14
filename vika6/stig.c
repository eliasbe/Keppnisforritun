#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAXN 100000 // 5000000
#define LEFT(x) ((x)*2)
#define RIGHT(x) ((x)*2 + 1)
int p[MAXN * 5], n;
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

int qrec(int i, int j, int x, int y, int e) // Hjálparfall.
{ // Við erum að leita að bili [x, y] og erum í [i, j].
  if (x == i && y == j)
    return p[e];
  int m = (i + j) / 2;
  if (x <= m && y <= m)
    return qrec(i, m, x, y, LEFT(e));
  if (x > m && y > m)
    return qrec(m + 1, j, x, y, RIGHT(e));
  return gcd(qrec(i, m, x, m, LEFT(e)), qrec(m + 1, j, m + 1, y, RIGHT(e)));
}
int query(int x, int y) { //
  return qrec(0, n - 1, x, y, 1);
}

void urec(int i, int j, int x, int y, int e) // Hjálparfall.
{ // Við erum að leita að laufinu [x, x] og erum í [i, j].
  if (i == j)
    p[e] = y;
  else {
    int m = (i + j) / 2;
    if (x <= m)
      urec(i, m, x, y, LEFT(e));
    else
      urec(m + 1, j, x, y, RIGHT(e));
    p[e] = gcd(p[LEFT(e)], p[RIGHT(e)]);
  }
}
void update(int x, int y) { // Látum x-ta stakið vera y.
  return urec(0, n - 1, x, y, 1);
}

int main() {
  int i, x, y, z, q, r;
  scanf("%d%d", &n, &q);
  for (i = 0; i < n; i++) {
    scanf("%d", &r);
    update(i, r);
  }
  for (i = 0; i < q; i++) {
    scanf("%d%d%d", &x, &y, &z);
    if (x == 1)
      update(y - 1, z);
    if (x == 2)
      printf("%d\n", query(y - 1, z - 1));
  }
  return 0;
}
