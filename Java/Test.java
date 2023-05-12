import java.util.*;
class A extends Thread {
    public void run() {
        try {
            for (int i = 0; i < 5; i++) {
                System.out.println("T1");
                Thread.sleep(100);
            }
        } catch (Exception e) {
        }
    }
}
class B extends Thread {
    public void run() {
        try {
            for (int i = 0; i < 5; i++) {
                System.out.println("T2");
                Thread.sleep(100);
            }
        } catch (Exception e) {
        }
    }
}
public class Test {
    public static void main(String[] args) {
        A a1 = new A();
        B b1 = new B();
        a1.start();
        b1.start();
        try {
            a1.join();
            b1.join();
            a1.setName("thread100");
        } catch (Exception e) {}
            System.out.println(a1.getName() + " " + b1.getName());
        
    }
}
