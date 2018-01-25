import java.util.*;
import java.io.*;
public class PrintPrimes{

public boolean isPrime(int num){
    boolean isPrime = true;
    for(int i=2;i<=num/2;i++){
    if(num%i==0)
    {
        isPrime = false;
        break;
    }
}
    return isPrime;
}    
public static void main(String[] args) {
    PrintPrimes obj = new PrintPrimes();
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the range: ");
    int num = sc.nextInt();
    for(int i=2; i<=num;i++){
        // System.out.printf("The number %d is Prime\n",i);

        if(obj.isPrime(i)){
            System.out.printf("The number %d is Prime\n",i);
        }
    }
}
}