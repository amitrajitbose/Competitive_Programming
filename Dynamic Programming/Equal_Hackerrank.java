/*
This problem was kept in the dynamic programming section, although I did not use DP
to solve it. My solution is linear time and much more efficient.
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the equal function below.
    static int findMin(int[] arr){
        int min = arr[0];
        int n = arr.length;
        for (int i=1;i<n;i++)
        {
            min = Math.min(min, arr[i]);
        }
        return min;
    }
    static int equal(int[] arr) {
        int [] shift = {0,1,2};
        int M = findMin(arr);
        int [] res = {0,0,0};
        for(int item: arr)
        {
            for(int i: shift)
            {
                int gap = item - M + i;
                res[i] += Math.floor(gap/5) + shift[(int)Math.floor(((gap % 5)+1)/2)];
            }
        }
    return findMin(res);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] arr = new int[n];

            String[] arrItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int arrItem = Integer.parseInt(arrItems[i]);
                arr[i] = arrItem;
            }

            int result = equal(arr);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}

