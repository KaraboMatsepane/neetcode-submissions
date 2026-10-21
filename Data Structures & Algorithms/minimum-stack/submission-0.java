class MinStack {

    List<List<Integer>> minStack;

    public MinStack() {
        minStack = new ArrayList<>();
    }
    
    public void push(int val) {
    
        if (minStack.isEmpty()){
            minStack.add(new ArrayList<>(List.of(val, val)));
        } else{

            List<Integer> prevPair = minStack.get(minStack.size() - 1);

            List<Integer> toAdd = new ArrayList<>();
            
            Integer prevMin = prevPair.get(0);

            Integer min = Math.min(prevMin, val);

            toAdd.add(min);
            toAdd.add(val);

            minStack.add(toAdd);
            
        }
        
    }
    
    public void pop() {
        minStack.remove(minStack.size() - 1);
    }
    
    public int top() {
        List<Integer> toReturn = minStack.get(minStack.size() - 1);

        return toReturn.get(1);
    }
    
    public int getMin() {
        List<Integer> toReturn = minStack.get(minStack.size() - 1);

        return toReturn.get(0);
    }
}
