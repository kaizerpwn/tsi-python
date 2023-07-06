#include <stdio.h>

void main()
{
    int niz[] = {-3,
                 0,
                 -1,
                 5,
                 2,
                 3,
                 0,
                 1};
    int trojke;
    for (int i = 0; i < 8; i++)
    {
        for (int j = i + 1; j < 8; j++)
        {
            for (int k = j + 1; k < 8; k++)
            {
                if (niz[i] + niz[j] + niz[k] == 0)
                {
                    if (niz[i] != niz[j] && niz[j] != niz[k] && niz[i] != niz[k] && niz[i] != -niz[j] && niz[j] != -niz[k] && niz[i] != -niz[k])
                        printf("%d + %d + %d = 0\n", niz[i], niz[j], niz[k]);
                    trojke++;
                }
            }
        }
    }
    printf("Broj trojki u ovom nizu je %d", trojke);
}