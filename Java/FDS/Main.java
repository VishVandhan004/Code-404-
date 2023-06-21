/* Write a Java program that takes an input array, finds a number
in the array which is a multiple of three, squares its index, 
and displays the result. 
The program takes the input array and index from the user
Sample input  output
Case 1:
Enter the size of the array: 5
Enter the array elements:
3 6 9 12 15
Enter the index: 4
The number at index 4 (which is a multiple of 3) is 12, and its index squared is 16.

Case 2:
Enter the size of the array: 3
Enter the array elements:8 9 2
Enter the index: 3
No number found at index 3 that is a multiple of 3.
*/
import java.util.*;
class test {
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        int size = sc.nextInt();
        System.out.print("Enter the array elements: ");
        int arr[] = new int[size];
        for(int i=0;i<size;i++)
        {
            arr[i] = sc.nextInt();
        }
        System.out.print("Enter the index: ");
        int ind = sc.nextInt();
        if(arr[ind-1]%3 == 0)
        {
            System.out.print("The number at index "+ ind +" (which is a multiple of 3) is "+ ind*3 +", and its index squared is "+ ind*ind +" ");
        }
        else {
            System.out.print("No number found at index "+ ind +" that is a multiple of 3");
        }
    }
}