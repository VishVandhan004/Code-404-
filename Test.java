import java.util.*;
public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of an array:");
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("Enter the no.of students");
        int m = sc.nextInt();
        Arrays.sort(arr);
        int min =Integer.MAX_VALUE;
        for(int i=0;i<=n-m;i++)
        {
            int diff = arr[i+m-1] - arr[i];
            if(diff<min)
            {
                min = diff;
            }
        }
        System.out.printf("Difference is %d",min);
    }
}
