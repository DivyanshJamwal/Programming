
import java.util.*;

public class prac_set {

    public static void main(String[] args) {
        
        int[] arr = {1, 3, 5, 2, 1, 3, 3, 4, 6, 7, 7};
        int n = 2;
        
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        
        List<Integer> result = new ArrayList<>();
        
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == n) {
                result.add(entry.getKey());
            }
        }
        
        System.out.println("Numbers that occur exactly " + n + " times: " + result);
    }
}
