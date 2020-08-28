// Make sure your class is public
public class Kata {
    public static double findUniq(double arr[]) {
      int count1 = 0,count2 = 0,index1=0,index2=0;
        double check = arr[0];
        for ( int i = 0 ; i < arr.length ; i++ ){
            if (check==arr[i]){
                count1++;
                index1=i;
            }
            else if (check!=arr[i]){
                count2++;
                index2=i;
            }
        }
        if (count1==1)
            return arr[index1];
        else if (count2==1)
            return arr[index2];
        return 0;
    }
}
