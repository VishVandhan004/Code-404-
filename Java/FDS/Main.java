import java.util.*;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String str = sc.nextLine();
        if(str.contains("Vijay")){
            str.replace("Vijay","Dinesh");
        }
    }
}