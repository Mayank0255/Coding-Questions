import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class WhichAreIn {

  public static String[] inArray(String[] array1, String[] array2) {
     Set<String> result = new HashSet<>();

     for(String a1 : array1) {
       for(String a2 : array2) {
         if(a2.contains(a1)) {
           result.add(a1);
           break;
         }
       }
     }

     String[] resultArray = result.toArray(new String[result.size()]);

     Arrays.sort(resultArray);

     return resultArray;
  }
}
