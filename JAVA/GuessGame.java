import java.util.*;
public class GuessGame {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int num = sc.nextInt();


while(num!=-1)
{
double p = Math.random();
p = (p*15)+1;
int x = (int)p;
if(x==num)
{
System.out.println("correct guess");
}
else
{
System.out.println("you're unlucky, the number is " + x);
}
num = sc.nextInt();
}
sc.close();

}
}
