#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#define EPS 1e-9

typedef double complex pt;

// Í hvora áttina er verið að beygja?
int ccw(pt a, pt b, pt c) {
  if (cabs(a - b) < EPS || fabs(cimag((c - a) / (b - a))) < EPS)
    return 0;
  return cimag((c - a) / (b - a)) > 0.0 ? 1 : -1;
}

pt piv;
// samanburðarfall til að raða eftir hornastærð
int cmp(const void *p1, const void *p2) {
  pt a = *(pt *)p1, b = *(pt *)p2;
  // Óþarfa athugun?
  if (fabs(carg(a - piv) - carg(b - piv)) > EPS)
    return carg(a - piv) < carg(b - piv) ? -1 : 1;
  if (fabs(cabs(a - piv) - cabs(b - piv)) < EPS)
    return 0;
  return cabs(a - piv) < cabs(b - piv) ? -1 : 1;
}

int convex_hull(pt *p, pt *h, int n) {
  // Eftir á er h kúpti hjúpur p. Skilar stærð h.
  int i, j = 0, mn = 0;
  for (i = 1; i < n; i++)
    if (cimag(p[i] - p[mn]) < 0.0 ||
        fabs(cimag(p[i] - p[mn])) < EPS && creal(p[i] - p[mn]) < 0.0)
      mn = i;
  pt t = p[mn];
  p[mn] = p[0];
  p[0] = t;
  piv = p[0];
  qsort(p + 1, n - 1, sizeof *p, cmp);
  for (i = 1; i < n && cabs(p[0] - p[i]) < EPS; i++)
    ;
  if (i == n)
    h[j++] = p[0];
  else if (i == n - 1)
    h[j++] = p[0], h[j++] = p[n - 1];
  if (i >= n - 1)
    return j;
  h[j++] = p[n - 1], h[j++] = p[0], h[j++] = p[i];
  if (ccw(h[0], h[1], h[2]) == 0)
    return j - (cabs(h[0] - h[1]) < EPS ? 2 : 1);
  for (i++; i < n;)
    (cabs(h[j - 1] - p[i]) > EPS && ccw(h[j - 2], h[j - 1], p[i]) == 1)
        ? (h[j++] = p[i++])
        : j--;
  return --j;
}

int main() {
  // int i, n, m;
  // double x, y;
  // scanf("%d", &n);
  // while (n != 0) {
  // pt a[n], h[n];
  // for (i = 0; i < n; i++) {
  // scanf("%lf%lf", &x, &y);
  // a[i] = x + y * I;
  // }
  char s[1000001], *a, *t;
  double complex real, imag;
  pt b[100], h[100];
  while (fgets(s, sizeof s, stdin)) {
    int i, n = 0;
    a = s, t = a + 1;
    while (*(a - 1) != '\n' && *(a - 1) != EOF) {
      real = strtod(a, &t), a = t + 1;
      imag = strtod(a, &t), a = t + 1;
      b[n] = real + imag * I;
      n++;
    }
    if (n == 0)
      break;
    // printf("input:\n");
    // for (i = 0; i < n; i++)
    // printf("%.3f %.3f\n", creal(b[n]), cimag(b[n]));

    int m;
    m = convex_hull(b, h, n);
    // printf("%d\n", m);
    // for (i = 0; i < m; i++)
    // printf("%d %d\n", (int)creal(h[i]), (int)cimag(h[i]));
    double ummal = 0.0;
    for (i = 0; i < m; i++)
      ummal += cabs(h[i] - h[(i + 1) % m]);
    // printf("%.10f\n", ummal);
    printf("%.10f\n", 100 * n / (1 + ummal));
  }
  return 0;
}
