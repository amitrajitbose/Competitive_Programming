#include <bits/stdc++.h>
using namespace std;

struct AdjaListNode
{
    int dest;
    struct AdjaListNode* next;
};
 
//adjacency list
struct AdjaList
{
    struct AdjaListNode *head;
    bool flag;
    AdjaList(){
    	flag = false;
    	head=NULL;
	}
};
 
//graph
struct Graph
{
    int V;
    struct AdjaList* array;
};
 
void resetflag(struct Graph* gph,int size){
	for (int i = 0; i < size; ++i)
       gph->array[i].flag = false;
}

struct AdjaListNode* newAdjaListNode(int dest)
{
    struct AdjaListNode* newNode =
            (struct AdjaListNode*) malloc(sizeof(struct AdjaListNode));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}
 
struct Graph* createGraph(int V)
{
    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
    graph->V = V;
    graph->array = (struct AdjaList*) malloc(V * sizeof(struct AdjaList));
    for (int i = 0; i < V; ++i)
       graph->array[i].head = NULL;
 
    return graph;
}
 
void insertPath(struct Graph* graph, int src, int dest)
{
    struct AdjaListNode* newNode = newAdjaListNode(dest);
    newNode->next = graph->array[src].head;
    
	graph->array[src].head = newNode;
    newNode = newAdjaListNode(src);
    
	newNode->next = graph->array[dest].head;
    graph->array[dest].head = newNode;
}

void travell(struct Graph* graph,int MasterNode[],std::queue<int> &q,int end,int v){
	struct AdjaListNode* trav = graph->array[v].head;
	graph->array[v].flag = true;
	int a;
	bool supa=false;
	while(trav){
		if(trav->dest==end) supa=true;
		if(!graph->array[trav->dest].flag){	
		q.push(trav->dest);
		MasterNode[trav->dest]=v;
		}
		trav = trav->next;
	}
	if(!supa){
	if(!q.empty()){
	a=q.front();
	q.pop();
	travell(graph,MasterNode,q,end,a);
	}}
}

void trace_back(int MasterNode[],int C[],int start, int v,int &max){
	
	if(MasterNode[v]!=start){
		C[MasterNode[v]]++;
		if(C[MasterNode[v]]>max) max=C[MasterNode[v]];
		trace_back(MasterNode,C,start,MasterNode[v],max);
	}
}

int main(){
	std::queue<int> queue_ra;
	int N,M;
    scanf("%d%d",&N,&M);
    int *C = (int *)calloc(N , sizeof(int));
    int *MasterNode = (int *)malloc(N * sizeof(int));
    struct Graph* graph = createGraph(N+1);
	int p1,p2;
    for(int i=0;i<N-1;i++){
    	
    	scanf("%d%d",&p1,&p2);
    	insertPath(graph, p1, p2);
	}
	int start,end;
	int max=C[1];
	for(int i=0;i<M;i++){
	scanf("%d%d",&start,&end);
	
	while(!queue_ra.empty()){
		queue_ra.pop();
	}
	resetflag(graph,N+1);
    travell(graph,MasterNode,queue_ra,end,start);	
    trace_back(MasterNode,C,start,end,max);
    C[start]++;C[end]++;
    if(C[start]>max) max=C[start];
    if(C[end]>max) max=C[end];
	}
	printf("%d",max);
	return 0;
}