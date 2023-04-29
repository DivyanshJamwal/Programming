import java.util.Scanner;

public class array3 {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);

char ch = sc.next().charAt(0);
char ch1 = sc.next().charAt(0);
sc.close();

if (ch >= 97 && ch <= 122 && ch1 >= 97 && ch1 <= 122 && ch < ch1) {
for (int i = (int) ch; i <= (int) ch1; i++) {
System.out.print((char) i + " ");
}
} else {
System.out.println("ERROR");
}
}
}