import javax.swing.*;

public class Or {
    public static void main(String[] args) {
        int primer_numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer numero"));
        int segundo_numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo numero"));
        if (primer_numero > 0 || segundo_numero >0){
            JOptionPane.showMessageDialog(null,"Primer numero: "+primer_numero+", Segundo numero: "+segundo_numero);
        }
    }
}
