import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Auto> autos = new ArrayList<>();
        Empleado employed1 = new Empleado("Sergio","Perez",1875000);
        Auto auto1 = new Auto("Toyota",2);
        Auto auto2 = new Auto("Mazda",1);
        Auto auto3 = new Auto("Tesla",1);
        autos.add(auto1);
        autos.add(auto2);
        autos.add(auto3);
        employed1.setAutos(autos);
        Empleado.calcularMiNomina(employed1);
        Concesionario.calcularPagos(employed1,"2020-01-01","2020-12-30");
        Concesionario.calcularDeducciones(employed1,"2020-01-01","2020-12-30");
        //Concesionario.calcularPagos(employed1,"2020-01-01","2020-12-30");
    }
}
