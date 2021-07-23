import javax.swing.*;

public class Cuadrado {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el un numero"));
        if(numero>0){
            numero = numero * numero;
            JOptionPane.showMessageDialog(null, "El cuadrado es: "+numero);
        }else{
            JOptionPane.showMessageDialog(null,"El numero es negativo");
        }
    }
}
