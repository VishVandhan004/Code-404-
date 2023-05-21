import java.util.*;
import java.util.Map;
import java.util.HashMap;
public class Main 
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int first = sc.nextInt();
        int second = sc.nextInt();
        String txt = sc.next();
        int age = sc.nextInt();
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
        // collections are framework in java
        // lists 
        ArrayList<String> al = new ArrayList<>();
        al.add("kia");
        al.add("MG");
        al.add("hyundai");
        int size = al.size();
        al.set(1,"toyota");
        al.remove(2);
        System.out.println(al);
        // maps
       Map bikes = new HashMap();
       bikes.put("Jupiter",2);
       bikes.put("ktm",1);
       System.out.println(bikes.get("ktm"));
       System.out.println(bikes);
       System.out.println("Welcome to the food app");
       System.out.println("Create a password");
       String pass1 = sc.next();
       System.out.println("your password is: "+ pass1);
       System.out.println("Enter your password");
       String pass = sc.next();
       while(!pass.equals(pass1)) {
        System.out.println("wrong password. try again");
        pass = sc.next();
    }
       System.out.println("granted");
       System.out.println("Are you hungry, yes or no");
       String ans = sc.next();
       if(ans.equals("yes")){
        
       }

    }
}
