public class Empleado {
    private int id;
    private final String nombre;
    private final String apellido;
    private final int comision;
    private final int horasExtra;
    private final int salario;

    public Empleado(String nombre, String apellido, int comision, int horasExtra, int salario){
        this.nombre = nombre;
        this.apellido = apellido;
        this.horasExtra = horasExtra;
        this.comision = comision;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getComision() {
        return comision;
    }

    public int getHorasExtra() {
        return horasExtra;
    }

    public int getSalario() {
        return salario;
    }

    public static double calcularMiNomina(Empleado empleado){
        double desvengado, total_desvengado, deducciones;

        desvengado = empleado.getSalario()+ empleado.getHorasExtra()+ empleado.getComision();
        deducciones = desvengado * 0.08;
        total_desvengado = desvengado - deducciones;
        return total_desvengado;
    }
}
