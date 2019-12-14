package model;

public class BibleText {
    private String livro;
    private int capitulo;
    private int versiculo;
    private String texto;

    @Override
    public String toString() {
        return "BibleText{" +
                "livro='" + livro + '\'' +
                ", capitulo=" + capitulo +
                ", versiculo=" + versiculo +
                ", texto='" + texto + '\'' +
                '}';
    }

    public String getLivro() {
        return livro;
    }

    public void setLivro(String livro) {
        this.livro = livro;
    }

    public int getCapitulo() {
        return capitulo;
    }

    public void setCapitulo(int capitulo) {
        this.capitulo = capitulo;
    }

    public int getVersiculo() {
        return versiculo;
    }

    public void setVersiculo(int versiculo) {
        this.versiculo = versiculo;
    }

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    public String getReferencia() {
        return getLivro() + " " + getCapitulo() + ":" + getVersiculo();
    }
}
