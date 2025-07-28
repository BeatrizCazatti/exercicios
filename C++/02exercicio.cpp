#include <iostream>
#include <cmath>

int main () {
    double area, raio;
    const double pi = 3.14;
    //A=piR²
    std::cout << "Raio: ";
    std::cin >> raio;
    area = floor(pi*pow(raio, 2));
    std::cout << "A area do circulo de raio " << raio << " eh " << area;
    return 0;
}