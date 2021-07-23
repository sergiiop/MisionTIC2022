import javax.swing.*;

public class test_postulante {
    public static void main(String[] args) {
        int numero_preguntas, total_preguntas;
        double porcentaje;
        String nivel = "";
        total_preguntas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el total de preguntas"));
        numero_preguntas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de preguntas respondidas correctamente"));
        porcentaje = (numero_preguntas * 100) / total_preguntas;
        if (porcentaje >= 90){
            nivel = "Nivel máximo";
        }else if (porcentaje >= 75 && porcentaje < 90){
            nivel = "Nivel medio";
        } else if (porcentaje >= 50 && porcentaje < 75){
            nivel = "Nivel regular";
        } else {
            nivel = "Fuera de nivel";
        }
        JOptionPane.showMessageDialog(null,"El postulado tiene un "+nivel+", con un "+porcentaje+"%");
    }
}
