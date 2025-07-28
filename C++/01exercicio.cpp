//Uma loja ganhou R$95.000 nas vendas e deve pagar x% de taxas estaduais e y% de taxas municipais.

#include <iostream>

using namespace std; // forma de evitar escrever std:: toda hora quando você usa funções ou objetos da biblioteca padrão do C++ (Standard Library – std).

int main (){
    double lucro = 95000, taxa_estado = 0, taxa_municipio = 0;

    cout << "Digite os valores das taxas estaduais e municipais: ";
    //cin >> taxa_estado;
    //cin >> taxa_municipio;
    cin >> taxa_estado >> taxa_municipio;

    cout << "Deve pagar R$" << (lucro*taxa_estado)/100 << " de taxas estaduais" << endl;
    cout << "Deve pagar R$" << (lucro*taxa_municipio)/100 << " de taxas municipais";
    
    return 0;
}
