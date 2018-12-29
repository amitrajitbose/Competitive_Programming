/*
https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
*/

{
//Initial Template for Java
import java.util.*;
class ModifyQueue{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int k=sc.nextInt();
            Queue<Integer> q=new LinkedList<>();
            while(n-->0){
                q.add((int)sc.nextInt());
            }
            GfG g=new GfG();
            Queue<Integer> ans=g.modifyQueue(q,k);
            while(!ans.isEmpty()){
                int a=ans.peek();
                ans.poll();
                System.out.print(a+" ");
            }
            System.out.println();
        }
    }
}
}

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

//User function Template for Java
class GfG
{
    public Queue<Integer> modifyQueue(Queue<Integer> q, int k)
    {
        Queue<Integer> tempqueue = new LinkedList<Integer>();
        Stack<Integer> tempstack = new Stack<Integer>();
        
        for(int i=0;i<k;i++)
        {
          tempstack.push(q.remove());
        }
        while(!q.isEmpty())
        {
          tempqueue.add(q.remove());
        }
        while(!tempstack.isEmpty())
        {
          q.add(tempstack.pop());
        }
        while(!tempqueue.isEmpty())
        {
          q.add(tempqueue.remove());
        }
        return q;
    }
}