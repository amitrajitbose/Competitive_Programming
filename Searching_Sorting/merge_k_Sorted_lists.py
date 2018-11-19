'''
Given k sorted arrays/lists, merge them into a 
single array
Ex: [1,4,7],[2,5,8],[3,6,9]

Time: O(kn*log(k))
'''
import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    
    heapq.heapify(heap)

    while heap:
        #print(heap)
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

#Test Cases
print(merge([[10,40,70],[20,50,80],[30,60,90]]))

print(merge([[],[],[]]))
print(merge([[1],[2],[3]]))
print(merge([[],[2],[]]))
print(merge([[1],[2,4],[3,5]]))
print(merge([[1,13,27,45],[2],[3,5,11,14,17,19,22]]))
