public class NumberFun {
  public static long findNextSquare(long sq) {

      long b = ((long)Math.sqrt(sq));
      if(b*b!=sq){
        return -1;
      }
        b++;
      return b*b;
  }
}
