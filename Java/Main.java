import java.io.*;
public class Main {
    public static void main(String[] args) {
        try {
            byte bwrite[] = {65,66,67,68,69};
            OutputStream os = new FileOutputStream("test.txt");
            for(int i=0;i<bwrite.length;i++){
                os.write(bwrite[i]);
            }
            InputStream is = new FileInputStream("test.txt");
            System.out.println("Available bytes in file:"+is.available());
            int line;
            while((line=is.read())!= -1){
                System.out.println((char)line);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
