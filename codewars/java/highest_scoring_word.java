public class Kata {
  public static String high(String s) {

    String[] arr = s.split("\\s+");
        int large = 0,index=0;

        for ( int i = 0 ; i < arr.length ; i++ ){
            int sum = 0;
            for (int j=0;j<arr[i].length();j++){
                sum+=((int)arr[i].charAt(j)-96);
            }
            
            if (sum>large){
                large = sum;
                index = i;
            }
        }
    return arr[index];
  }
}
