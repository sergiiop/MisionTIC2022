import javax.swing.*;

public class Notas {
    public static void main(String[] args) {
        float nota_1,nota_2,nota_3;
        double nota_definitiva;
        nota_1 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la primera nota"));
        nota_2 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la segunda nota"));
        nota_3 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la tercera nota"));
        nota_definitiva = (nota_1 + nota_2 + nota_3) / 3;
        if(nota_definitiva >= 3){
            JOptionPane.showMessageDialog(null,"La nota definitiva es: "+nota_definitiva+", el estudiante gana la materia");
        }else{
            JOptionPane.showMessageDialog(null,"La nota definitiva es: "+nota_definitiva+", el estudiante pierde la materia");
        }
    }
}
