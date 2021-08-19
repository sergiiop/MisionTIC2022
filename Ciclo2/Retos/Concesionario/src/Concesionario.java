import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

public class Concesionario {
    private ArrayList<Auto> autos = new ArrayList<>();
    private ArrayList<Empleado> empleados = new ArrayList<>();

    public ArrayList<Auto> getAutos() {
        return autos;
    }

    public void setAutos(ArrayList<Auto> autos) {
        this.autos = autos;
    }

    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }
    public static long calcularDiasLaborados(String ingreso, String retiro){
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyy-MM-dd");
        LocalDate d1 = LocalDate.parse(ingreso,formatter);
        LocalDate d2 = LocalDate.parse(retiro,formatter);
        long days = d1.until(d2).getMonths() * 30 + d1.until(d2).getDays();
        return days;

    }

    public static float calcularPagos(Empleado empleado, String ingreso, String retiro){
        int comision = Empleado.calcularMiComision(empleado);
        long diasLaborados = Concesionario.calcularDiasLaborados(ingreso, retiro);
        int pagoPorDia = empleado.getSalario()/30;
        long pagos =((pagoPorDia*diasLaborados)+comision);
        System.out.println(pagos);
        return pagos;
    }

    public static double calcularDeducciones(Empleado empleado, String ingreso, String retiro){
        float pages = calcularPagos(empleado,ingreso,retiro);
        float deductions = pages * 0.08F;
        System.out.println(deductions);
        return deductions;
    }
}
