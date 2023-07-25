import java.util.*;
class test {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        A = A.substring(0, 1).toUpperCase() + A.substring(1);
        B = B.substring(0, 1).toUpperCase() + B.substring(1);
        int len1 = A.length();
        int len2 = B.length();
        System.out.println(len1+len2);
        int result = A.compareTo(B);
        if(result < 0){
            System.out.println("No");
        } else {
            System.out.println("Yes");
        }
        System.out.print(A+" "+B);
    }
}