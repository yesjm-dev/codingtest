import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {

    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> days = new LinkedList<>();

        for (int i = 0; i < progresses.length; i++) {
            int day = (int)Math.ceil((100 - progresses[i]) / (double)speeds[i]);
            days.offer(day);
        }

        List<Integer> answers = new ArrayList<>();
        while (!days.isEmpty()) {
            int current = days.poll();
            int count = 1;

            while (!days.isEmpty() && days.peek() <= current) {
                days.poll();
                count++;
            }
            answers.add(count);
        }
        
        return answers.stream().mapToInt(i -> i).toArray();
    }

}