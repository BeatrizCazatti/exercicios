#include <iostream>

int main () {
    int a = 1, b = 2;
    std::cout << "Hello World!\n";

    //Swap
    int temp = a;
    a = b;
    b = temp;

    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b;

    return 0;
}