// https://leetcode.com/problems/my-calendar-iii

class MyCalendarThree {
    TreeMap<Integer, Integer> delta;

    public MyCalendarThree() {
        delta = new TreeMap();
    }

    public int book(int start, int end) {
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);

        int active = 0, ans = 0;
        for (int d: delta.values()) {
            ans = Math.max(ans, active += d);
        }
        return ans;
    }
}

/*
Reference:

.getOrDefault()
---------------
Returns the value to which the specified key is mapped, or defaultValue if this map contains no mapping for the key.
In this case the default value is 0, the key is start/end respectively.
For more: 
https://docs.oracle.com/javase/8/docs/api/java/util/Map.html
https://docs.oracle.com/javase/7/docs/api/java/util/TreeMap.html
*/
