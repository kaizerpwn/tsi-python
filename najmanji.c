#include <stdio.h>

int fibonacci(int n)
{
    if (n > 1)
        return fibonacci(n - 2) + fibonacci(n - 1);
}

int fibonacciArray(int n)
{
    int broj1 = 1, broj2 = 1, trenutni;
    for (int i = 0; i < n; i++)
    {
        if(i <= 1) broj2 = i;
        trenutni = (broj1+broj2);
        broj1 = broj2;
        broj2 = trenutni;
        if(i == n-1) return trenutni;
    }
}

void main()
{
    int niz[10] = {4, 8, 12, 13, 68, 7, 2, 12, 9, 77};
    int najmanji = niz[0];
    for (int i = 0; i < 10; i++)
    {
        if (najmanji > niz[i])
            najmanji = niz[i];
    }
    printf("Najmanji element u nizu je %d\n", najmanji);

    int broj;
    printf("Unesite neki broj za fibonaccijev niz\n");
    scanf("%d", &broj);

    int rezultat = fibonacci(broj);

    printf("Rezultat fibonaccijevog niza je %d\n", rezultat);
    int rezultatFibonacci = fibonacciArray(broj);

    printf("Rezultat fibonaccijevog niza petljom je : %d", rezultatFibonacci);
}
