import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};
        
        Map<String, Integer> users = new HashMap<>();
        for (String id : id_list) {
            users.put(id, 0);
        }
        
        Set<String> uniqueReports = new HashSet<>(Arrays.asList(report));
        for (String ur : uniqueReports) {
            String[] parts = ur.split(" ");
            String reportedUser = parts[1];
            users.put(reportedUser, users.get(reportedUser) + 1);
        }

        Map<String, Integer> reportCount = new HashMap<>();
        for (String ur : uniqueReports) {
            String[] parts = ur.split(" ");
            String reportingUser = parts[0];
            String reportedUser = parts[1];
            if (users.get(reportedUser) >= k) {
                reportCount.put(reportingUser, reportCount.getOrDefault(reportingUser, 0) + 1);
            }
        }
        
        for (String id : id_list) {
            answer = Arrays.copyOf(answer, answer.length + 1);
            answer[answer.length - 1] = reportCount.getOrDefault(id, 0);
        }

        return answer;
    }


}