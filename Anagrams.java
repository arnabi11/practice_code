import java.util.*;
import java.util.Scanner;
// import java.Collections.*;
public class Anagrams{
    public static void main(String[] args) {
    
 
         
         Scanner sc=new Scanner(System.in);
         String s1=sc.nextLine();
         String s2=sc.nextLine();
        char[]sorted1=(s1.toCharArray());
        char[]sorted2=(s2.toCharArray());
        Arrays.sort(sorted1);
        Arrays.sort(sorted2);

        if(sorted1.length== sorted2.length)
        {
            System.out.println("array 1 "+ new String(sorted1));
            System.out.println("array 2 "+ new String(sorted2));
            for(int i=0; i<sorted1.length; i++)
            {
            if(sorted1[i]==sorted2[i])
            {continue;}
            else{
                System.out.println("1no");
                return;
                }    
            }
            System.out.println("yes");
        
        }
        else
        {
            System.out.println("2no");
        }
    }
     
    
}