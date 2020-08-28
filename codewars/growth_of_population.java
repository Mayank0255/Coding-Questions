class Arge {

    public static int nbYear(int p0, double percent, int aug, int p) {
        int tp=p0,i=0;
        while (tp<p){
            double avg = (tp*percent)/100;
            tp=tp + (int)avg + aug;
            i++;
        }
        return i;
    }
}
