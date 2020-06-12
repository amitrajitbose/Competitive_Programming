class RandomizedSet {
    Map<Integer, Integer> hash;
    List<Integer> arr;

    /** Initialize your data structure here. */
    public RandomizedSet() {
        this.hash = new HashMap<>();
        this.arr = new ArrayList<>();
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. in O(1) */
    public boolean insert(int val) {
        if (!hash.containsKey(val)) {
            arr.add(val);
            hash.put(val, arr.size()-1);
            return true;
        }
        return false;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. in O(1)*/
    public boolean remove(int val) {
        if (!hash.containsKey(val)) {
            return false;
        }
        int lastEle = arr.get(arr.size()-1);
        int idx = hash.get(val);
        arr.set(idx, lastEle);
        hash.put(lastEle, idx);
        arr.remove(arr.size()-1);
        hash.remove(val);
        return true;
    }

    /** Get a random element from the set. in O(1) */
    public int getRandom() {
        return arr.get(getRandomNumber(0, arr.size()-1));
    }

    /** Get a random number between min and max. */
    private int getRandomNumber(int min, int max) {
        return (int)(Math.random() * (max - min + 1) + min);
    }

    /** Search for presence of a value in O(1) */
    public boolean search(int val) {
        return hash.containsKey(val);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */