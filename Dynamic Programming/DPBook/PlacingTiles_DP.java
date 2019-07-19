/*
Given an empty plot of size 2*n, we want to place some tiles such
that entire plot is covered. Each tile is of size 2*1 and can be
placed either horizontally or vertically. Write a function to return
the total possible ways of placing the tiles
*/

/*
Solution:

Way 1: Place one tile vertically. Remaining area = 2*(n-1)
Way 2: Place first tile horizontally, on top of it another horizontal
    tile has to be placed (we have no other option), remaining plot
    2*(n-2)

So if n=1, there is 1 possible way
If  n==2, there are 2 possible ways (both Horizontal, or both vertical)

the recursion looks like this

f(n)
{
    if n IS 0 -> RET 0
    if n IS 1 -> RET 1
    if n IS 2 -> RET 2
    ELSE RET -> f(n-1)+f(n-2)
}

Rings a bell?
Yes, this is same as fibonacci sequence. Easy huh! ;)
*/

public static int placeTiles_2N(int n)
{
    // Bottom Up DP Solution
    if (n<3)
        return n;
    else
    {
        int a = 1;
        int b = 2;
        int c;
        for (int i=3; i<=n; i++)
        {
            c = a+b;
            a = b;
            b = c;
        }
        return c;
    }
}

/*
Follow Up
---------
If the size of the plot is changed to 3*n, then what changes do we
need to make in our solution. The tiles are each of 2*1, same as
before.
*/

/*
If n=1, there are no possible ways, so 0

If n=2, there are 3 possible ways as follows:
(A) 3 Horizontally
(B) 2 Vertical Above 1 Horizontal
(C) 2 Vertical Below 1 Horizontal

*/

public static int placeTiles_3N(int n)
{
    // Bottom Up DP Solution
    if (n<=1)
        return 0;
    if (n==2)
        return 3;
    else
    {
        int a = 1;
        int b = 3;
        int c;
        for (int i=3; i<=n; i++)
        {
            c = a+b;
            a = b;
            b = c;
        }
        return c;
    }
}