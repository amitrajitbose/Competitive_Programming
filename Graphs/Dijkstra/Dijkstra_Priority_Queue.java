class Pair
{
    int node,weight;
    public Pair(int n,int w)
    {
        weight = w;
        node = n;
    }
}

public class Solution {
    public static int INF = 99999;
    public ArrayList<Integer> solve(int A, ArrayList<ArrayList<Integer>> B, int C) {
        ArrayList<ArrayList<Pair>> adj = new ArrayList<>();
        for(int i = 0 ; i < A; i++)
            adj.add(new ArrayList<>());
        for(int i = 0 ; i < B.size() ; i++)
        {
            adj.get(B.get(i).get(0)).add(new Pair(B.get(i).get(1) , B.get(i).get(2)));
            adj.get(B.get(i).get(1)).add(new Pair(B.get(i).get(0) , B.get(i).get(2)));
        }
        
        int distance[] = new int[A];
        Arrays.fill(distance,INF);
        distance[C] = 0;
       
        PriorityQueue<Integer> pq = new PriorityQueue<>( (p1,p2) -> distance[p1] - distance[p2]  );
        for(int i = 0 ; i < A ; i++)
            pq.add(i);
        
        while(!pq.isEmpty())
        {
            int minNodeReached = pq.peek();
            pq.poll();
            for(Pair p : adj.get(minNodeReached))
            {
                int nd = p.node;
                int wt = p.weight;
                if(distance[nd] > distance[minNodeReached] + wt){
                    distance[nd] = distance[minNodeReached] + wt;
                    pq.add(p.node);
                }
            }
            
        }
        
        for(int i = 0 ; i < A; i++)
            if(distance[i] == INF)
                distance[i] = -1;
        
        ArrayList<Integer> x = new ArrayList<>();
        
        for(int i = 0 ; i < A; i++)
            x.add(distance[i]);
            
        return x;
        
    }
}

