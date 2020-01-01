package model;

import exceptions.QueryBibleException;
import helper.DbController;
import helper.StringHelper;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;

public class Bible {
    private String livro;
    private int capitulo;
    private int versiculo;
    private String texto;
    private String versao;

    public void avancarVersiculo() throws QueryBibleException {
        query(livro + " " + capitulo + " " + (versiculo + 1), versao);
    }

    public void voltarVersiculo() throws QueryBibleException {
        query(livro + " " + capitulo + " " + (versiculo - 1), versao);
    }

    public void query(String q, String versao) throws QueryBibleException {
        this.versao = versao;
        try {
            q = q.replace(":", " ");
            q = q.replace("  ", " ");

            q = StringHelper.normalizar(q);
            ArrayList<String> livCapVer = new ArrayList<>(Arrays.asList(q.split(" ")));

            String ver = livCapVer.get(livCapVer.size() - 1);
            livCapVer.remove(livCapVer.size() - 1);
            String cap = livCapVer.get(livCapVer.size() - 1);
            livCapVer.remove(livCapVer.size() - 1);
            String liv = String.join(" ", livCapVer);

            String sql = addJoin(
                    "versao = '" + versao + "' AND livros._sigla like '%" + liv + "%' AND textos.capitulo = " + cap + " AND textos.versiculo = " + ver + ""
            );
            ResultSet resultSet = DbController.query(sql);

            if (!resultSet.next()) {
                sql = addJoin(
                        "versao = '" + versao + "' AND livros._nome like '%" + liv + "%' AND textos.capitulo = " + cap + " AND textos.versiculo = " + ver + ""
                );
                resultSet = DbController.query(sql);
            }

            this.setLivro(resultSet.getString("livro"));
            this.setCapitulo(resultSet.getInt("capitulo"));
            this.setVersiculo(resultSet.getInt("versiculo"));
            this.setTexto(resultSet.getString("texto"));
        } catch (SQLException e) {
            throw new QueryBibleException("Texto inexistente");
        } catch (Exception e) {
            e.printStackTrace();
            throw new QueryBibleException("Pesquisa inválida");
        }
    }

    public static ArrayList<String> getVersoes() {
        try {
            ArrayList<String> versoes = new ArrayList<>();
            ResultSet resultSet = DbController.query("SELECT versao FROM versoes");
            while (resultSet.next()) {
                versoes.add(resultSet.getString("versao"));
            }
            return versoes;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    private static String addJoin(String s) {
        return "SELECT versoes.versao as versao, livros.nome as livro, textos.capitulo, textos.versiculo, textos.texto " +
                "FROM textos " +
                "JOIN livros on textos.id_livro = livros.id " +
                "JOIN versoes on textos.id_versao = versoes.id " +
                "WHERE " + s;
    }

    public static ArrayList<String> getLivrosBiblia() {
        ArrayList<String> livros = new ArrayList<>();

        try {
            ResultSet resultSet = DbController.query("SELECT nome FROM livros ORDER BY id");
            while (resultSet.next()) {
                String livro = resultSet.getString("nome");
                livros.add(livro);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return livros;
    }

    @Override
    public String toString() {
        return "Bible{" +
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

    public String getTextWithReference() {
        return getTexto() + " (" + getReferencia() + ")";
    }
}
