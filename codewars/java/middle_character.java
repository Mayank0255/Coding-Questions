class Kata {
  public static String getMiddle(String word) {
    if ( word.length()%2 == 1 )
        return word.substring(word.length()/2,word.length()/2+1);
    else if ( word.length()%2 == 0 )
        return word.substring(word.length()/2-1,word.length()/2+1);
    return "";
  }
}
