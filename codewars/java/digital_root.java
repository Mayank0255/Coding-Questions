public class DRoot {
    
  public static int digital_root(int n) {
    int sum=0;
    while (n>9){
        sum=0;
        while (n>0){
            sum += n%10;
            n=n/10;
        }
        n = sum;
     }
     return sum;
  }
}
