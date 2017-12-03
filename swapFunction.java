import java.util.*;


class swapFunction{
    int a , b;
    public static void  swapFunc(swapFunction obj){
        int x= obj.a;
        obj.a=obj.b;
        obj.b=x;
        System.out.println("i = "+obj.a+" j="+ obj.b);
        

    }
    public static void main(String[] args) {
        swapFunction obj = new swapFunction();
        obj.a = 10;
        obj.b=20;
        swapFunc(obj );
        // String s1 = "Hello World";
        // char[] arr = s1.toCharArray();
        System.out.println("i = "+obj.a+" j="+obj.b);
    }
}