class dem{
    static dem d;
    private dem(){

    }
    static dem getInstance(){
    d = new dem();
    return d;
    }
}

public class singleton {
    public static void main(String[] args) {
        dem d = dem.getInstance();
        System.out.println(d);
    }
}
