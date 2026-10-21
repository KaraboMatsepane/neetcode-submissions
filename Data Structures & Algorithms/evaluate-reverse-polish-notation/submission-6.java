class Solution {
    public int evalRPN(String[] tokens) {

        Deque<Integer> stack = new ArrayDeque<>();
        Deque<Integer> evaluations = new ArrayDeque<>();

        int lastEvaluation = Integer.parseInt(tokens[0]);

        for (int i = 0; i < tokens.length; i++){
            String current = tokens[i];

            if (current.matches("-?\\d+")){
                stack.push(Integer.parseInt(current));
                continue;
            }

            int first;
            int second;

            if (stack.isEmpty()) return lastEvaluation;

            second = stack.pop();
            first = stack.pop();

            lastEvaluation = switch (current) {
                case "+"-> first + second;

                case "-"-> first - second;
                
                case "*" -> first * second;
                default -> {
                    if (second == 0) yield 0;
                    else yield first / second;
                }
            };

            stack.push(lastEvaluation);

        }

        return lastEvaluation;
        
    }
}
