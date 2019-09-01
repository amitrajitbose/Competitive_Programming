/*
Given an array A, generate an array B such that
B[i] is the next lower element present after the next higher element of A[i] with respect to array A
If no such element is present, B[i] will be -1.

Sample:
{3,1,7,8,4} -> {4,4,4,-1,-1}
Explanation:
4 is the next lower element that comes after 7 which is the next greater element with respect to 3
4 is the next lower element that comes after 7 which is the next greater element with respect to 1
4 is the next lower element that comes after 8 which is the next greater element with respect to 7
-1 because 8 has no next greater element and thus no next lower
-1 because 4 has no next greater element and thus no next lower
*/

import java.util.*;
public class MyClass {
    // Author = @amitrajitbose
    public static void main(String args[]) {
      int arr1[] = {3,1,7,8,4}; // {4 4 4 -1 -1}
      //int arr1[] = {2,4,8,7,6,5}; // {-1 7 -1 -1 -1 -1}
      int[] res1 = nextHighLow(arr1);
      for(int i = 0; i < arr1.length; i++){
          System.out.print(res1[i]+" ");
      }
      System.out.println();
    }
    public static int[] nextHighLow(int[] arr1){
      Map<Integer, Integer> greater = NGE(arr1);
      Map<Integer, Integer> lesser = NLE(arr1);
      int[] res1 = new int[arr1.length];
      for(int i = 0; i < arr1.length; i++){
          int nge = greater.get(arr1[i]);
          if (nge == -1){
              res1[i] = -1;
          }
          else{
              res1[i] = lesser.get(nge);
          }
      }
      return res1;
    }
    public static Map NGE(int[] arr){
        if (arr.length <= 0){
            return null;
        }
        Deque<Integer> st = new ArrayDeque<>(); //stack
        Map<Integer, Integer> map = new HashMap<>(); //solution set
        st.push(0);
        int popped;
        for(int i=1; i<arr.length;i++){
            while(!st.isEmpty() && arr[st.peek()] < arr[i]){
                popped = st.pop();
                map.put(arr[popped], arr[i]);
            }
            st.push(i);
        }
        while(!st.isEmpty()){
            popped = st.pop();
            map.put(arr[popped],-1);
        }
        return map;
    }
    public static Map NLE(int[] arr){
        if (arr.length <= 0){
            return null;
        }
        int n = arr.length;
        Deque<Integer> st = new ArrayDeque<>(); //stack
        Map<Integer, Integer> map = new HashMap<>(); //solution set
        st.push(0);
        int popped;
        for(int i=1; i<arr.length;i++){
            while(!st.isEmpty() && arr[st.peek()] > arr[i]){
                popped = st.pop();
                map.put(arr[popped], arr[i]);
            }
            st.push(i);
        }
        while(!st.isEmpty()){
            popped = st.pop();
            map.put(arr[popped],-1);
        }
        return map;
    }
}

