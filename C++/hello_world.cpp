#include <iostream>

int main () {
    int a = 1, b = 2;
    std::cout << "Hello World!";

    //Swap
    int temp = a;
    a = b;
    b = temp;

    std::cout << a;
    std::cout << b;

    return 0;
}