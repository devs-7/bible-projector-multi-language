package helper;

import exceptions.QueryBibleException;
import model.BibleText;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.Normalizer;
import java.util.ArrayList;
import java.util.Arrays;

public class Bible {
    public static BibleText query(String q, String versao) throws QueryBibleException, SQLException {
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

            BibleText bibleText = new BibleText();
            bibleText.setLivro(resultSet.getString("livro"));
            bibleText.setCapitulo(resultSet.getInt("capitulo"));
            bibleText.setVersiculo(resultSet.getInt("versiculo"));
            bibleText.setTexto(resultSet.getString("texto"));
            return bibleText;
        } catch (SQLException e) {
            throw new SQLException(e);
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
}
