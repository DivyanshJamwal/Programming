package Coding_Practice.JAVA;

class Demo {
    int a; int b;
    String st1; String st2;
    Demo() {
    a = 0;
    b = 0;
    st1 = null;
    st2 = null;
    }
    Demo(int a, int b) {
    this();
    this.a = a;
    this.b = b;
    }
    Demo(String a, String b) {
    this(2,3);
    st1 = a;
    st2 = b;
    System.out.println(this.a+this.b);
    System.out.println(st1+st2);
    }
    }
    class HelloWorld {
    public static void main(String[] args) {
    Demo d3 = new Demo("Hello"," world");
    System.out.println(d3);
    }
    }