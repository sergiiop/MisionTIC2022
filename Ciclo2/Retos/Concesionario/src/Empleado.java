import java.util.ArrayList;

public class Empleado {
    private int id;
    private String nombre;
    private String apellido;
    private ArrayList<Auto> autos = new ArrayList<>();
    private int salario;

    public Empleado(String nombre, String apellido, int salario){
        this.nombre = nombre;
        this.apellido = apellido;
        this.salario = salario;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public ArrayList<Auto> getAutos() {
        return autos;
    }

    public void setAutos(ArrayList<Auto> autos) {
        this.autos = autos;
    }

    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }

    public static double calcularMiNomina(Empleado empleado){
        double total = 0,deductions, commission;

        commission = calcularMiComision(empleado);
        System.out.println(commission);
        System.out.println(empleado.getSalario());
        total = empleado.getSalario()+commission;
        deductions = total * 0.08;
        total -= deductions;
        return total;
    }

    public static int calcularMiComision(Empleado empleado){
        int AUTO_TIPO_1, AUTO_TIPO_2,AUTO_TIPO_3, comision = 0;
        AUTO_TIPO_1 = 750000;
        AUTO_TIPO_2 = 500000;
        AUTO_TIPO_3 = 350000;

        for(int i= 0;i < empleado.getAutos().size();i++ ){
            if(empleado.getAutos().get(i).getTipo() == 1) {
                comision += AUTO_TIPO_1;
            }else if(empleado.getAutos().get(i).getTipo() == 2) {
                comision += AUTO_TIPO_2;
            }else if(empleado.getAutos().get(i).getTipo() == 3){
                comision += AUTO_TIPO_3;
            }
        }
        return comision;
    }
}
