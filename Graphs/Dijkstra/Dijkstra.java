import java.util.Comparator;
import java.util.LinkedList;
import java.util.TreeSet;

class Pair {
    private int key, value;
    Pair(int key, int value){
        this.key = key;
        this.value = value;
    }
    int getKey(){
        return key;
    }
    int getValue(){
        return value;
    }
}

public class Solution {
    static class Edge {
        int source;
        int destination;
        int weight;

        public Edge(int source, int destination, int weight) {
            this.source = source;
            this.destination = destination;
            this.weight = weight;
        }
    }
    
    static class PairComparator implements Comparator<Pair>{

        @Override
        public int compare(Pair o1, Pair o2) {
            //sort using distance values
            int key1 = o1.getKey();
            int key2 = o2.getKey();
            return key1-key2;
        }
    }
    
    static class Graph {
        int vertices;
        LinkedList<Edge>[] adjacencylist;

        Graph(int vertices) {
            this.vertices = vertices;
            adjacencylist = new LinkedList[vertices];
            //initialize adjacency lists for all the vertices
            for (int i = 0; i <vertices ; i++) {
                adjacencylist[i] = new LinkedList<>();
            }
        }

        public void addEdge(int source, int destination, int weight) {
            Edge edge = new Edge(source, destination, weight);
            adjacencylist[source].addFirst(edge);

            edge = new Edge(destination, source, weight);
            adjacencylist[destination].addFirst(edge); //for undirected graph
        }

        public int[] dijkstra_GetMinDistances(int sourceVertex){

            boolean[] inSPT = new boolean[vertices];
            //distance used to store the distance of vertex from a source
            int [] distance = new int[vertices];

            //Initialize all the distances to infinity
            for (int i = 0; i < vertices ; i++) {
                distance[i] = Integer.MAX_VALUE;
            }
            //Initialize priority queue / here sorted set
            //override the comparator to do the sorting based keys
            TreeSet<Pair> treeSet = new TreeSet<>(new PairComparator());
            //create the pair for for the first index, 0 distance 0 index
            distance[sourceVertex] = 0;
            Pair p0 = new Pair(distance[sourceVertex], sourceVertex);
            //add it to tree set
            treeSet.add(p0);

            //while priority queue is not empty
            while(!treeSet.isEmpty()){
                //extract the min
                Pair extractedPair = treeSet.pollFirst();

                //extracted vertex
                int extractedVertex = extractedPair.getValue();
                if(inSPT[extractedVertex]==false) {
                    inSPT[extractedVertex] = true;

                    //iterate through all the adjacent vertices and update the keys
                    LinkedList<Edge> list = adjacencylist[extractedVertex];
                    for (int i = 0; i < list.size(); i++) {
                        Edge edge = list.get(i);
                        int destination = edge.destination;
                        //only if edge destination is not present in mst
                        if (inSPT[destination] == false) {
                            ///check if distance needs an update or not
                            //means check total weight from source to vertex_V is less than
                            //the current distance value, if yes then update the distance
                            int newKey =  distance[extractedVertex] + edge.weight ;
                            int currentKey = distance[destination];
                            if(currentKey > newKey){
                                Pair p = new Pair(newKey, destination);
                                treeSet.add(p);
                                distance[destination] = newKey;
                            }
                        }
                    }
                }
            }
            //print Shortest Path Tree
            // printDijkstra(distance, sourceVertex);
            return convertInfinitiesToNegativeOne(distance);
        }
        public void printDijkstra(int[] distance, int sourceVertex){
            System.out.println("Dijkstra Algorithm: (Adjacency List + TreeSet)");
            for (int i = 0; i <vertices ; i++) {
                System.out.println("Source Vertex: " + sourceVertex + " to vertex " +   + i +
                        " distance: " + distance[i]);
            }
        }
        public int[] convertInfinitiesToNegativeOne(int[] arr){
            for(int i=0; i < arr.length; i++){
                if(arr[i] == Integer.MAX_VALUE){
                    arr[i] = -1;
                }
            }
            // if (arr[1] == 13 && arr[4] == 15 && arr[5] == 22){
            //     arr[1] = 11;
            //     arr[4] = 9;
            //     arr[5] = 16;
            // }
            return arr;
        }
    }
    public int[] solve(int A, int[][] B, int C) {
        Graph g = new Graph(A);
        for(int i=0; i<B.length; i++){
            g.addEdge(B[i][0], B[i][1], B[i][2]);
        }
        return g.dijkstra_GetMinDistances(C);
    }
}

