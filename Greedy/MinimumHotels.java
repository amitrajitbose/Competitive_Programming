/*
Hackerrank : https://www.hackerrank.com/contests/booking-womenintech/challenges/minimum-hotels
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Complete the solve function below.
    static int solve(List<Integer> customers, int k) {
        Set<Integer> hSet = new HashSet<>(); 
        hSet.addAll(customers);
        List<Integer> customer = new ArrayList<>(hSet); // list with duplicates removed
        Collections.sort(customer);
        int pos = customer.get(0) + k;
        int hotels = 1;
        
        for (int i: customer){
            if (Math.abs(pos - i) > k){
                hotels++;
                pos = i + k;
            }
        }
        return hotels;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int customerCount = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> customer = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                    .map(Integer::parseInt)
                    .collect(toList());

                int k = Integer.parseInt(bufferedReader.readLine().trim());

                int result = solve(customer, k);

                bufferedWriter.write(String.valueOf(result));
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

