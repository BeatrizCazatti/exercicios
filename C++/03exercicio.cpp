//Simulador de dado

#include <iostream>
#include <cstdlib>
#include <ctime>

int main () {
    const int maxValue = 6, minValue = 1;
    srand(time(0));
    int dado = (rand() % (maxValue - minValue +1)) + 1;
    std::cout << "Tirou " << dado << " no dado!";
    return 0;
}