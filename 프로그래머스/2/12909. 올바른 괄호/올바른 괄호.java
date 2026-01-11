class Solution {

    boolean solution(String s) {
        if (s.charAt(0) == ')' || s.charAt(s.length() - 1) == '(')
            return false;
        
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') count++;
            else if (c == ')') count--;
            if (count < 0) return false;
        }

        return count == 0;
    }

}