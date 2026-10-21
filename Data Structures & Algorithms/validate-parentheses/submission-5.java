class Solution {
    public boolean isValid(String s) {


    Map<Character, Character> pairs = new HashMap<>();

    Deque<Character> stack = new ArrayDeque<>();

    pairs.put(')', '(');
    pairs.put('}', '{');
    pairs.put(']', '[');

    for (char ch: s.toCharArray()) {
        if (pairs.containsKey(ch)) {
            if (!stack.isEmpty() && pairs.get(ch) == stack.peek()) stack.pop();
            else return false;
        } else {
            stack.push(ch);
        }
    }

    return stack.isEmpty();
        
    }
}
