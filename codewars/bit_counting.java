public class BitCounting {

  public static int countBits(int n){
    int count=0,a;
        String x="";
        while(n > 0) {
            a = n % 2;
            if(a == 1)
            {
                count++;
            }
            x = a + "" + x;
            n = n / 2;
        }
        
        return count;
  }
}
