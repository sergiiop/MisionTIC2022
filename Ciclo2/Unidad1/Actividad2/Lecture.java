import java.util.Scanner;

public class Lecture {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese un numero: ");
        int numero = entrada.nextInt();
        if (numero > 0){
            System.out.println("Feliz día");
        }
        else if(numero == 0){
            System.out.println("Vamos muy bien");
        }
        else {
            System.out.println("Para atrás ni para coger impulso");
        }
    }
}
