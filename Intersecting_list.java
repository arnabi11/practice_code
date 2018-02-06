import java.io.*;
class ListNode {
      int val;
      ListNode next;
      ListNode(int x) {
          val = x;
          next = null;
      }
 }
public class Intersecting_list{
    public static void main (String[] args) {
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(3);
        list1.next.next.next = new ListNode(4);
        list1.next.next.next.next = new ListNode(5);
        list1.next.next.next.next.next = new ListNode(6);
        list1.next.next.next.next.next.next = new ListNode(7);
        
        ListNode list2 = new ListNode(8);
        list2.next = list1.next.next.next;

        getIntersectionNode(list1,list2);
        getIntersectionNode1(list1,list2);
    }
    public static int getIntersectionNode1(ListNode headA, ListNode headB){
        ListNode l1 = headA;
        ListNode l2= headB;
        int c1=0,c2=0;
        while(l1!= null){
            c1++;
            l1 =  l1.next;
        }
        while(l2!= null){
            c2++;
            l2 =  l2.next;
        }
        int diff = Math.abs(c2-c1);
        System.out.println(diff);
        l1=headA;
        l2=headB;
        if(c2>c1)
        {
            for(int i=0; i<diff; i++){
                l2=l2.next;
            }
        }
        else
        {
           for(int i=0; i<diff; i++){
                l1=l1.next;
            } 
        }
        while(l1!=null)
        {
            if(l1.next==l2.next){
                System.out.println("yes "+l1.next.val);
                return 1;
            }
        }
        System.out.println("no");
        return 0;
    }
    public static int getIntersectionNode(ListNode headA, ListNode headB) {
        
        ListNode l1=headA, l2=headB;
        if (l1 == null || l2 == null)
            return 0;
        while(l2 != null){
            while(l1!=null){
                if(l1.next == l2.next){
                    System.out.println("Yes " + l2.next.val);
                    return 1;
                }
                else{
                    l1 = l1.next;
b                }
            }
            l2 = l2.next;
            l1 = headA;
        }
        System.out.println("No ");
        return 0;
    }
}