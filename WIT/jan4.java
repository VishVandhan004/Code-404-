import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class jan4 {
    public static void main(String[] args) {
        try {
            // Load the driver class
            Class.forName("com.mysql.cj.jdbc.Driver");
            // Get the connection
            Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "username", "password");
            String insertSql = "INSERT INTO employees (name, age) VALUES (?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(insertSql);
            preparedStatement.setString(1, "John");
            preparedStatement.setInt(2, 30);
            int rowsAffected = preparedStatement.executeUpdate();
            System.out.println("Rows inserted: " + rowsAffected);
            preparedStatement.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
