package helper;

import java.io.File;
import java.net.URL;
import java.sql.*;

public class DbController {
    public static Connection getConnection() throws SQLException {
        try {
            File file = new File(DbController.class.getClassLoader().getResource("bible.db").getFile());
            Class.forName("org.sqlite.JDBC");
            return DriverManager.getConnection("jdbc:sqlite:" + file.getPath());
        } catch (ClassNotFoundException e) {
            throw new SQLException(e.getMessage());
        }
    }

    public static Statement getStatement() throws SQLException {
        return getConnection().createStatement();
    }

    public static void execute(String sql) throws SQLException {
        getStatement().execute(sql);
    }

    public static ResultSet query(String sql) throws SQLException {
        PreparedStatement stmt = DbController.getConnection().prepareStatement(sql);
        ResultSet resultSet = stmt.executeQuery();
        return resultSet;
    }
}
