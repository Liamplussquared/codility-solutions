import java.util.*;

class Solution {
    public int solution(String S) {
        Stack<Character> stack = new Stack<Character>();
        char temp;
        if (S.length() == 0) {
            return 1;
        }
        
        for(int i = 0; i < S.length(); i++){
            temp = S.charAt(i);
            switch(temp) {
                case '}':
                    if (stack.isEmpty() || stack.pop() != '{'){
                        return 0;
                    }
                    break;
                case ']':
                    if (stack.isEmpty() || stack.pop() != '['){
                        return 0;
                    }
                    break;
                case ')':
                    if (stack.isEmpty() || stack.pop() != '('){
                        return 0;
                    }
                    break;
                default:
                    stack.push(temp);
                    break;
            }
        }
        if (stack.size() == 0) 
            return 1;
        else 
            return 0;
    }
}