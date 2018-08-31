# Network Flow Algorithm
**Aim** - To maximize the total amount of fluid flowing from source to sink.

### What is the flow network?
A *directed* graph in which each edge (u,v) in the edge set has a *non-negative* **capacity**. Capacity is defined as the maximum limit of flow that can be allowed to flow through the path/pipe. We ignore/remove any self-loops. For our convenience, we assume that the **source** has no incoming edges, the **sink** has no outgoing edges. Every node in the graph lies on some path from *source* to *sink*.

### Constraints
**Flow Constraint** - For all edges (u,v) between source and sink, the sum of flows for all *(u,v)* is equals to sum of all flows for all *(v,u)*. For an (u,v) which is not an edge, the flow is zero.

**Capacity Constraint** - For all edges, flow is 0 <= f(u,v) <= c(u,v), where c is the capacity. Thus maximum flow is equal to the capacity, minimum flow equal to zero.

CLRS: *The capacity constraint simply says that the flow from one vertex to another must be nonnegative and must not exceed the given capacity. The flow-conservation property says that the total flow into a vertex other than the source or sink must equal the total flow out of that vertex—informally, “flow in equals flow out.”*


