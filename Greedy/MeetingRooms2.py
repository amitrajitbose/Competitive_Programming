# https://leetcode.com/problems/meeting-rooms-ii

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ts = []
        for i in intervals:
            ts.append([i[0], "S"])
            ts.append([i[1], "E"])
        ts.sort(key=lambda x: (x[0], x[1]))
        # it is important to note here that E is lexicographically smaller than S
        # therefore when at a given time one meeting starts and another meeting ends we prioritize the ending meeting first so the same room can be reused
        room = 0
        maxroom = 0
        for t in ts:
            if t[1] == "S":
                room += 1
            else:
                room -= 1
            maxroom = max(maxroom, room)
        return maxroom
