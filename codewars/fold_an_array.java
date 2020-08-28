import java.util.Arrays;
import java.util.stream.IntStream;


public class Kata {

  public static int[] foldArray(int[] array, int runs) {
    final int[] result = Arrays.copyOfRange(array, 0, Math.round(array.length / 2.0f));

    IntStream.range(0, array.length / 2)
             .forEach(i -> result[i] = array[i] + array[array.length - 1 - i]);

    return runs > 1 ? foldArray(result, --runs) : result;
  }
}
