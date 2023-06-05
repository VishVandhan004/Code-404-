import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int size = sc.nextInt();
        System.out.println("Enter the elements:");
        int arr[] = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("enter the target:");
       int target = sc.nextInt();
       for (int i = 0; i < size; i++) {
        if(arr[i] == target){
            System.out.println(i);
        }
       }
        sc.close();
    }
}
