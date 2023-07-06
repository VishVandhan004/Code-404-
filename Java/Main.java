import java.io.FileInputStream;
import java.io.IOException;
public class Main {
    public static void main(String[] args) {
        try {
            FileInputStream file = new FileInputStream("abc.txt");
            int size = file.available();
            byte[] data = new byte[size];
            file.read(data);
            file.close();
            String fileContent = new String(data);
            System.out.println("Contents of the file:");
            System.out.println(fileContent);
        } catch (IOException e) {
            System.out.println("Exception occurred: " + e.getMessage());
        }
    }
}
