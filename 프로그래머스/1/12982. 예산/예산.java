import java.util.Arrays;
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;

        int[] arr = Arrays.stream(d).sorted().toArray();

        for (int i : arr) {
            if (budget - i >= 0) {
                budget -= i;
                answer++;
            } else {
                break;
            }
        }
        return answer;
    }
}