#include <stdio.h>
int greedy_check(int *x, int n, int k, int m)
{
    int i, j, r = 0;
    for (i = 0, j = 0; i < n; i++)
    {
        if (j + x[i] > m) r++, j = 0; 
        j += x[i];
    }
    r++;
    return r <= k;
}
int main()
{
    int i, r, s, n, k;
    scanf("%d%d", &n, &k);
    int x[n];
    s = 0;
    r = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &x[i]); 
        s += x[i];
        if (x[i] > r) r = x[i];
    }
    while (r < s)
    {
        int m = (r + s)/2;
        if (greedy_check(x, n, k, m)) s = m;
        else r = m + 1;
    }
    printf("%d\n", r);
    return 0;
}
