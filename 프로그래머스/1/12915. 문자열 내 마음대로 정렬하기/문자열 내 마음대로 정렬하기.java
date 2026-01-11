import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String[] solution(String[] strings, int n) {
        List<String> answer = Arrays.stream(strings)
            .sorted()
            .sorted(Comparator.comparing(s -> s.charAt(n))
            ).collect(Collectors.toList());
        
        return answer.toArray(new String[0]);
    }
}