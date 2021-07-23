import javax.swing.*;

public class Tipo_numero {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        if(numero > 0){
            JOptionPane.showMessageDialog(null, "el numero "+numero+ " es positivo");
        } else if (numero == 0) {
            JOptionPane.showMessageDialog(null, "el numero "+numero+ " es neutro");
        } else{
            JOptionPane.showMessageDialog(null, "el numero "+numero+ " es negativo");
        }
    }
}
