package com.ib;

import java.util.ArrayDeque;
import java.util.Deque;

public class MinStack {
    Deque<Integer> stack;
    Integer minele;

    MinStack(){
        stack = new ArrayDeque<>();
        minele = 0;
    }

    public void push(int x) {
        if(stack.isEmpty()){
            minele = x;
            stack.offerFirst(x);
        }
        else {
            if (x < minele) {
                stack.push(2 * x - minele);
                minele = x;
            } else {
                stack.push(x);
            }
        }
    }

    public void pop() {
        if(!stack.isEmpty()) {
            Integer t = stack.removeFirst();
            if (t < minele){
//                return minele; // since pop() does not return anything
                minele = 2*minele - t;
            }
        }
    }

    public int top() {
        return stack.isEmpty() ? -1 : Math.max(minele, stack.peek());
    }

    public int getMin() {
        return stack.isEmpty() ? -1 : minele;
    }
}

