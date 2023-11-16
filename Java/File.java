/*  
In a primary school mathematics teacher has given a task to students, i.e multiply all the integers between 1 to n and give the final product.With a pen and paper, this process has taken much more time,and you are thier computer teacher can you help students by giving a program to solve this task.

input format = integer
output format = integer
    
	Example 1:
	input=5
	output=120

	Example 2:
	input=6
	output=720
	
	Example 3:
	input=8
	output=40320
*/
import java.util.*;
class File {
    public static int fact(int n){
        if(n==0){
            return 1;
        }
        else if(n==1){
            return 1;
        }
        else {
            return n*fact(n-1);
        }
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = fact(n);
        System.out.print(result);
    }
}