#include <math.h>
#include <stdio.h>
#define EPS 1e-6

int main() {
  double n, a, b, x, m;
  a = 0.0;
  scanf("%lf", &n);
  b = 11.0;
  x = 0.0;
  m = 0.0;
  while ((abs(n - x) > EPS) & (abs(a - b) > 1e-12)) {
    m = (a + b) / 2.0;
    x = pow(m, m);
    if (x > n)
      b = m;
    else
      a = m;
  }
  printf("%#.10f\n", m);
  return 0;
}
