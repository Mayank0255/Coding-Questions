public class SpinWords {

  public String spinWords(String sentence) {
        String[] splited = sentence.split("\\s+");
        String[] res = new String[splited.length];
        StringBuffer ans = new StringBuffer();

        for (int i=0; i<splited.length; i++){
            if (splited[i].length()>=5) {
                StringBuffer sb = new StringBuffer(splited[i]);
                res[i] = sb.reverse().toString();
            }
            else {
                res[i] = splited[i];
            }
        }

        for (int i=0; i<res.length; i++) {
            if (i!=res.length-1) {
                ans.append(res[i]+" ");
            }
            else if (i==res.length-1) {
                ans.append(res[i]);
            }
        }
        return ans.toString();
  }
}
