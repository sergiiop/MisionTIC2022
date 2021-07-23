import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num_1, num_2, option;
        float resultado = 0;
        System.out.println("Operaciones Disponibles para realizar: " +
                "\n1)Suma\n2)Resta\n3)Multiplicación\n4)División \n5)Residuo \n6) Salir.");
        System.out.print("Elija una opción: ");
        option = in.nextInt();
        if(option == 6){
            System.out.println("Hasta Pronto");
        }
        else if (option >=0 && option <=5){
            System.out.print("Ingrese el primer Valor: ");
            num_1 = in.nextInt();
            System.out.print("Ingrese el segundo Valor: ");
            num_2 = in.nextInt();
            switch (option){
                case 1:
                    resultado = num_1 + num_2;
                    break;
                case 2:
                    resultado = num_1 - num_2;
                    break;
                case 3:
                    resultado = num_1 * num_2;
                    break;
                case 4:
                    if(num_2!=0){
                        resultado = num_1 / num_2;
                    }else{
                        System.out.println("Error al realizar la operación");
                        System.exit(0);
                    }
                    break;
                case 5:
                    resultado = num_1 % num_2;
                    break;
                default:
                    System.out.println("Entrada Incorrecta");
                    break;
            }
            if (option <= 5){
                System.out.println("El resultado de la operación es: "+resultado);
            }
        } else{
            System.out.println("Entrada Incorrecta");
        }

    }
}
