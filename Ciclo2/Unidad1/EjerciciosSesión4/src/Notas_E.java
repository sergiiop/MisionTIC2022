import javax.swing.*;

public class Notas_E {
    public static void main(String[] args) {
        float nota1,nota2,nota3;
        double definitiva;
        nota1 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la primera nota"));
        if(nota1 >=0 && nota1 <= 5){
            nota2 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la segunda nota"));
            if(nota2 >=0 && nota2 <= 5){
                nota3 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la tercera nota"));
                if(nota3 >=0 && nota3 <= 5){
                    definitiva = (nota1+nota2+nota3) / 3;
                    if(definitiva >= 3){
                        JOptionPane.showMessageDialog(null,"El estudiante Gana la materia con un promedio de "+definitiva);
                    }else{
                        JOptionPane.showMessageDialog(null,"El estudiante Pierde la materia con un promedio de "+definitiva);
                    }
                }else {
                    JOptionPane.showMessageDialog(null,"Error en la nota");
                }
            }else {
                JOptionPane.showMessageDialog(null,"Error en la nota");
            }
        }else {
            JOptionPane.showMessageDialog(null,"Error en la nota");
        }
    }
}
