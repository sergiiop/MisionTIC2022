public class Auto {
    private String marca;
    private int tipo;

    public Auto(String marca, int tipo) {
        this.marca = marca;
        this.tipo = tipo;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setTipo(int tipo) {
        this.tipo = tipo;
    }

    public String getMarca() {
        return marca;
    }

    public int getTipo() {
        return tipo;
    }
}
