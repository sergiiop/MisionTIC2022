import javax.swing.*;

public class SalarioPorHora {
    public static void main(String[] args) {
        double salario, salario_neto;
        int num_horas;
        salario = Double.parseDouble(JOptionPane.showInputDialog("Ingrese su salario por hora"));
        num_horas = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero de horas trabajadas"));
        salario_neto = salario * num_horas;
        if(salario_neto > 200000){
            JOptionPane.showMessageDialog(null, "El trabajador gana más de $200.000");
        }else{
            JOptionPane.showMessageDialog(null, "El trabajador gana menos de $200.000");
        }
    }
}
