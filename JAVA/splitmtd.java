public class splitmtd {
    public static void main(String[] args) {
        String str = "BMW,Mercedes,Mclaren,Porsche";
        String[]a = str.split(",",-2);
        for(String x: a)
        System.out.println(x);
    }
}
