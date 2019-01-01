'''
DCP #21

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def min_rooms(start, end):
    start = sorted(start)
    end = sorted(end)
    n = len(start)
    min_room = 1
    room_needed = 1
    i = 1
    j = 0
    while(i<n and j<n):
        #print(room_needed)
        if(start[i] <= end[j]):
            #extra room will be needed for this event
            room_needed += 1
            i += 1
            min_room = max(min_room, room_needed)
        else:
            #can be hosted in the same room
            room_needed -= 1
            j += 1
    return min_room
            
for _ in range(int(input())):
    n = int(input())
	events = [(30, 75), (0, 50), (60, 150)]
    start = []
    end = []
	for i in events:
		start.append(i[0])
		end.append([[1])
    print(min_rooms(start, end))
