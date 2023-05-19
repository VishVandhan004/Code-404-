import java.util.*;
public class Main 
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int first = sc.nextInt();
        int second = sc.nextInt();
        String txt = sc.next();
        int age = sc.nextInt();
        sc.close();
        System.out.println(first + second);
        System.out.println(first - second);
        System.out.println(first * second);
        System.out.println(first * second);
        System.out.println(first / second);
        System.out.println(first % second);
        System.out.println(txt);
        if(age>18 && age<80)
        {
            System.out.println("You can drive");
        }
        else {
            System.out.println("Don't drive");
        }
        int a = 9;
        char ch = 'w';
        String str = "Java";
        boolean b = true;
        double d = 69.69;
        System.out.println(d);
        System.out.println(b);
        System.out.println(str);
        System.out.println(ch);
        System.out.println(a);
        System.out.println("Hello world");
    }
}
