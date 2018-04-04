#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <ctime>
using namespace std;

// Esta funcion recursiva retorna el N-esimo  numero  de  la  secuencia  de  Fibbonacci
int fibonacci(int N)
{
    if(N == 0 || N == 1)
        return N;
    else
        return fibonacci(N-1) + fibonacci(N-2);
}

// Esta funcion retorna el tiempo (en segundos) que se tarda en obtener el N-esimo numero de la secuencia de Fibbonacci
float get_time(int N)
{
    clock_t t;
    t = clock();
    int a = fibonacci(N);
    t = clock() - t;
    float time = ((float)t)/CLOCKS_PER_SEC;
    return time;
}

int main()
{
    // Imprime el tiempo (en segundos) que se tarda en obtener el N-esimo numero de la secuencia de Fibbonacci para los primeros 35 valores de N
    for(int i; i<35; i++)
    {
        float t = get_time(i);
        printf("%i %f \n", i, t);
    }
    return 0;
}
