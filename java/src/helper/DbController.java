package helper;

import java.io.File;
import java.io.IOException;
import java.sql.*;

public class DbController {
    public static Connection getConnection() throws SQLException {
        try {
            Class.forName("org.sqlite.JDBC");
            String path = new File("..\\data\\bible.db").getCanonicalPath();
            System.out.println("############################");
            System.out.println(path);
            return DriverManager.getConnection("jdbc:sqlite:" + path);
        } catch (ClassNotFoundException e) {
            throw new SQLException(e.getMessage());
        } catch (IOException e) {
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
