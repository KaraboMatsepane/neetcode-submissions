class Solution {
    public boolean isValid(String s) {

        if (s.length() % 2 != 0) return false;

        Deque<Character> stack = new ArrayDeque<>();

        for (char ch: s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
                continue;
            }

            if (stack.isEmpty()) return false;

            char pair = stack.pop();

            if (ch == ')'){
                if (pair != '(') return false;
            } else if (ch == '}'){
                if (pair != '{') return false;
            } else {
                if (pair != '[') return false;
            }

        }

        return stack.isEmpty();
    }
}
