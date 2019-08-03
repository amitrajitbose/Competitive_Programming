public static int editDist(String a, String b)
{
	int m = a.length();
	int n = b.length();
	int editmat[][] = new int[m+1][n+1];
	// for top row
	for(int i=0; i<=n; i++)
		editmat[0][i] = i;
	// for left column
	for(int i=0; i<=m; i++)
		editmat[i][0] = i;
	for(int i=1; i<=m; i++)
	{
		for(int j=1; j<=n; j++)
		{
			// if two characters are same
			if(a.charAt(i-1) == b.charAt(j-1))
				editmat[i][j] = editmat[i-1][j-1];
			else{
				editmat[i][j] = Math.min(editmat[i][j-1], (Math.min(editmat[i-1][j], editmat[i-1][j-1]))) + 1;
			}
		}
	}
	return editmat[m][n];
}
public static void main(String args[])throws IOException
{
	String a = "COMPUTER";
	String b = "COMMUTER";
	System.out.println(editDist(a,b));
}

