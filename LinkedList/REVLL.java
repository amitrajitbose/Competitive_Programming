/*package whatever //do not write package name here */
/*
Problem Link : https://www.codechef.com/problems/REVLL
*/
import java.io.*;
import java.util.*;

class Node{
    private int data;
    Node prev;
    Node next;
    
    Node(int data){
        this.data = data;
        this.prev = null;
        this.next = null;
    }
    
    int getData(){
        return this.data;
    } 
}

class DLL{
    Node head;
    Node tail;
    int size;
    boolean reversed;
    
    DLL(){
        head = new Node(0);
        tail = new Node(0);
        this.size = 0;
        this.reversed = false;
        head.next = tail;
        tail.prev = head;
    }
    
    int getsize(){
        return this.size;
    }
    
    void addFirst(int newdata)
    {
        Node newnode = new Node(newdata);
        if (this.size == 0){
            // Adding first node
            this.head.next = newnode;
            this.tail.prev = newnode;
            newnode.prev = this.head;
            newnode.next = this.tail;
        }
        else if(! this.reversed){
            this.head.next.prev = newnode;
            newnode.next = this.head.next;
            newnode.prev = this.head;
            this.head.next = newnode;
        }
        else if(this.reversed){
            this.tail.prev.next = newnode;
            newnode.prev = this.tail.prev;
            newnode.next = this.tail;
            this.tail.prev = newnode;
        }
        this.size += 1;
    }
    
    void addLast(int newdata)
    {
        Node newnode = new Node(newdata);
        if (this.size == 0){
            // Adding first node
            this.head.next = newnode;
            this.tail.prev = newnode;
            newnode.prev = this.head;
            newnode.next = this.tail;
        }
        else if(! this.reversed){
            this.tail.prev.next = newnode;
            newnode.prev = this.tail.prev;
            newnode.next = this.tail;
            this.tail.prev = newnode;
        }
        else if(this.reversed){
            this.head.next.prev = newnode;
            newnode.next = this.head.next;
            newnode.prev = this.head;
            this.head.next = newnode;
        }
        this.size += 1;
    }
    
    int removeFirst(){
        if(this.size == 0){
            System.out.println("ListEmptyException");
            return 0;
        }
        if(! this.reversed){
            Node removedNode = this.head.next;
            this.head.next = this.head.next.next;
            this.size -= 1;
            return removedNode.getData();
        }
        else{
            Node removedNode = this.tail.prev;
            this.tail.prev = this.tail.prev.prev;
            this.size -= 1;
            return removedNode.getData();
        }
    }
    
    int removeLast(){
        if(this.size == 0){
            System.out.println("ListEmptyException");
            return 0;
        }
        if(! this.reversed){
            Node removedNode = this.tail.prev;
            this.tail.prev = this.tail.prev.prev;
            this.size -= 1;
            return removedNode.getData();
        }
        else{
            Node removedNode = this.head.next;
            this.head.next = this.head.next.next;
            this.size -= 1;
            return removedNode.getData();
        }
    }
    
    int getFirst(){
        if(! this.reversed)
            return this.head.next.getData();
        else
            return this.tail.prev.getData();
    }
    
    int getLast(){
        if(! this.reversed)
            return this.tail.prev.getData();
        else
            return this.head.next.getData();
    }
    
    void reverse()
    {
        this.reversed = !this.reversed;
    }
    
    void show()
    {
        if(this.size == 0){
            System.out.println("null");
        }
        else{
            if(! reversed){
                Node ptr = this.head.next;
                while (ptr.next!=null){
                    System.out.print(ptr.getData()+"->");
                    ptr = ptr.next;
                }
                System.out.println("null");
            }
            else{
                Node ptr = this.tail.prev;
                while (ptr.prev!=null){
                    System.out.print(ptr.getData()+"->");
                    ptr = ptr.prev;
                }
                System.out.println("null");
            }
        }
    }
}
class Main{
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        while(tc-- > 0){
            int queries = Integer.parseInt(br.readLine());
            DLL mylist = new DLL();
            while(queries-- > 0){
                String[] inp = br.readLine().trim().split(" ");
                //System.out.println("Processing Query..."+inp[0]+"..Size="+mylist.getsize());
                if(inp[0].compareTo("I")==0){
                    System.out.println(mylist.getsize() == 0);
                }
                else if(inp[0].compareTo("AF")==0){
                    int data = Integer.parseInt(inp[1]);
                    mylist.addFirst(data);
                    mylist.show();
                }
                else if(inp[0].compareTo("AL")==0){
                    int data = Integer.parseInt(inp[1]);
                    mylist.addLast(data);
                    mylist.show();
                }
                else if(inp[0].compareTo("F")==0){
                    System.out.println(mylist.getFirst());
                }
                else if(inp[0].compareTo("L")==0){
                    System.out.println(mylist.getLast());
                }
                else if(inp[0].compareTo("RF")==0){
                    int tmp = mylist.removeFirst();
                    mylist.show();
                }
                else if(inp[0].compareTo("RL")==0){
                    int tmp = mylist.removeLast();
                    mylist.show();
                }
                else if(inp[0].compareTo("REV")==0){
                    mylist.reverse();
                    mylist.show();
                }
            }
        }
    }
}