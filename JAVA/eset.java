import java.util.HashMap;
import java.util.Map;
import java.util.Set;
public class eset {
    public static void main(String[] args) {

        HashMap<String, Integer> hashMap = new HashMap<>();
        

        hashMap.put("apple", 1);
        hashMap.put("banana", 2);
        hashMap.put("orange", 3);
        

        Set<Map.Entry<String, Integer>> entries = hashMap.entrySet();
        for (Map.Entry<String, Integer> entry : entries) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println(key + " -> " + value);
        }
        
    }
}
