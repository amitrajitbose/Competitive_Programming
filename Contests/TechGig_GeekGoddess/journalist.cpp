
/*
Contest link: https://www.techgig.com/geekgoddess

A journalist (100 Marks)
A millionaire from London bought a unique house, which is having lot of rooms, expensive items and many other automatic equipment. A journalist went to his house for interviewing him. He entered the wrong door and comes inside the house but he lost his path for going to main room due to lot of rooms and unique structure of house. He got stuck into the house. He goes from one room to another, but couldn't find the right door. He got one automatic answer machine in a room and asked it about way to go out. Machine replied that he will receive a word but he needs to make a proper pattern from that word. After entering the pattern in the machine, he will get the correct path from machine. By this way, he can come out of the house. Word Pattern should be made, if we start word from the left letter to the right or from the right to left, then that word should be same. For making this type of pattern, he can add as many letters in the word at any place.

You need to tell, how many minimum number of characters he needs to add in the original word for making this type of pattern.      


Input Format
First line  represents total number of characters in the word, which is of integer type N. 
Second line represents a word, which is of string type containing alphabets and digits only which is case-sensitive.


Constraints
3<=N<=5000

Output Format
You need to print desired minimum number of characters needs to add in the original word.


Sample TestCase 1
Input
5
Ab3bd
Output
2
Explanation
After adding two characters 'd' after 'A' and 'A' at the last of the given word, now the word will be "Adb3bdA", Hence the output will be 2.
*/
/* Read input from STDIN. Print your output to STDOUT*/
#include <bits/stdc++.h>
using namespace std;
int table[5001][5001];
int minCharInsertPalin(char str[], int n)
{
	int l, h, gap;
	memset(table, 0, sizeof(table));
	for (gap = 1; gap < n; ++gap)
		for (l = 0, h = gap; h < n; ++l, ++h)
			table[l][h] = (str[l] == str[h])? table[l+1][h-1]:(min(table[l][h-1], table[l+1][h])+1);
	return table[0][n-1];
}
int main(int argc, char *a[])
{
    int n;
    cin >> n;
	char str[5001];
	cin >> str;
	printf("%d", minCharInsertPalin(str, n));
	//cout << minCharInsertPalin(str, n);
	return 0;
}
/*
Author: Amitrajit Bose
https://amitrajitbose.github.io
*/