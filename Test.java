import java.util.*;

public class Test {
    
        public static String foo(){
            System.out.println("Test toString called");
            return "";
        }
        
        public static void main(String args[]){
            Test trst = null;
            System.out.println(trst.foo());
        }
    }