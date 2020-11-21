import java.util.Arrays;

public class Kata {
    public static int findShort(String s) {
      String[] words = s.split("\\s+");
        for (int i = 0; i < words.length; i++) {
            words[i] = words[i].replaceAll("[^\\w]", "");
        }
        int len=words[0].length();
        for (int i=1;i<words.length;i++){
            if ( words[i].length() < len ){
                len = words[i].length();
            }
        }
        return len;

    }
}
