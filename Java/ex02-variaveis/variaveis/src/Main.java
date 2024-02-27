public class Main {
    public static void main(String[]args) {
        int idade = 18;
        System.out.println("A idade é " + idade + " anos.");

        double tamanho = 1.64;
        System.out.println("Meu tamanho é " + tamanho + "m.");

        //obs: quando fazemos operações entre inteiros o resultado sempre será inteiro e não de ponto flutuante.
        double primeiraDivisão = 5/2;
        System.out.println(primeiraDivisão);

        double segundaDivisão = 5.0/2;
        System.out.println(segundaDivisão);

        long numeroGrande = 200000000000L;
        short numeroMédio = 1000;
        byte numeroPequeno = 100;
        System.out.println(numeroPequeno + " " + numeroMédio + " " + numeroGrande);

        //converter tipos primitivos de variáveis:
        double salario = 2570.50;
        System.out.println(salario);

        int valor = (int) salario;
        System.out.println(valor);
    }

}