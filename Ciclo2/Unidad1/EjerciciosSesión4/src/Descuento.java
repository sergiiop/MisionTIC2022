import javax.swing.*;

public class Descuento {
    public static void main(String[] args) {
        double valor_compra, descuento, total_compra;
        int numero;
        valor_compra = Double.parseDouble(JOptionPane.showInputDialog( "Ingrese el valor de la compra:"));
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero:"));
        if (numero < 74){
            descuento = valor_compra * 0.15;
        }else{
            descuento = valor_compra * 0.2;
        }
        total_compra = valor_compra - descuento;
        JOptionPane.showMessageDialog(null, "El valor descontado es: $"+descuento+", el valor total es: $"+total_compra);
    }
}
