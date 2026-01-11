import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        Set<Integer> phoneketmon = new HashSet<>();

        for (int i : nums) {
            phoneketmon.add(i);
        }

        return Math.min(nums.length / 2, phoneketmon.size());
    }
}