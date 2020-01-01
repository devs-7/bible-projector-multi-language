package model;

public class Livro {
    private String nome;
    private int[] nVersosPorCapitulo;

    public Livro(String nome, int[] nVersosPorCapitulo) {
        this.nome = nome;
        this.nVersosPorCapitulo = nVersosPorCapitulo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int[] getnVersosPorCapitulo() {
        return nVersosPorCapitulo;
    }

    public void setnVersosPorCapitulo(int[] nVersosPorCapitulo) {
        this.nVersosPorCapitulo = nVersosPorCapitulo;
    }
}
