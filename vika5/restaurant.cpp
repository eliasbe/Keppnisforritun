#include <assert.h>
#include <iostream>
#include <list>
#include <stdio.h>
#define MAXN 100
#define MAXC 1000
#define MAXM 1000
#define MAXS 30001

int min(int a, int b) {
  if (a < b)
    return a;
  return b;
}

bool jafnt = 0;
int minnun[MAXN][MAXS], virdi[MAXN], bakk[MAXN][MAXS];
int lookup(int i, int s) {
  if (s == 0)
    return 0;
  if (s < 0)
    return 1;
  if (i == MAXN)
    return 1;
  if (minnun[i][s] != -1)
    return minnun[i][s];

  int vera = lookup(i, s - virdi[i]);
  int fara = lookup(i + 1, s);

  if (vera == 0 && fara == 0)
    jafnt = 1;

  return minnun[i][s] = min(vera, fara);
}

void orders(int *C, int *S, int n, int m) {
  for (int o = 0; o < m; o++) {
    int i, j;
    for (i = 0; i < n; i++) {
      for (j = 0; j < MAXS; j++)
        minnun[i][j] = -1, bakk[i][j] = -1;
      virdi[i] = C[i];
    }
    jafnt = 0;

    int tokst = lookup(0, S[o]);

    if (tokst != 0)
      printf("Impossible");
    else if (jafnt)
      printf("Ambiguous");
    else {
      std::list<int> order;

      int ess = S[o];
      i = 0;
      while (ess > 0) {
        if (bakk[i][ess] == 0)
          order.push_front(i + 1), ess -= virdi[i];
        else
          i++;
      }
      order.sort();
      // printf("%d\t", order);
      for (int item : order)
        std::cout << item << " ";
    }
  }
}

int main() {
  int n, m, i, j, C[MAXN], S[MAXS];
  scanf("%d", &n);
  for (i = 0; i < n; i++)
        scanf("%
