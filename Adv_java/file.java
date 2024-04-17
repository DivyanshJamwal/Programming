import java.nio.file.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.*;
import java.util.*;
// import java.util.*;

// class file
// {
// public static void main(String args[]) throws IOException
// {
// Path p=Paths.get("k21bp.txt");
// Files.delete(p);
// System.out.println("File deleted");
// }
// }


// class file {
// public static void main(String args[]) {
// try {
// Path p=Paths.get("k21bp");
// if(Files.exists(p)) {
// System.out.println("Directory already exists");
// }
// else
// {
// Path p2=Files.createDirectory(p);
// System.out.println("Directory created at "+ p2);
// }
// }
// catch(Exception e){
// e.printStackTrace();}}}

// class file {
// public static void main(String args[]) {
// try {
// Path p1=Paths.get("k21bp\\firstfile.txt");
// if(Files.exists(p1)) {
// System.out.println("File already exists");
// }
// else
// {
// Path p2=Files.createFile(p1);
// System.out.println("File created at "+ p2.toString());
// }
// }
// catch(Exception e){
// e.printStackTrace();}}}


// class file {
// public static void main(String args[]) {
// try {
// Path p1=Paths.get("k21bp\\secondfile.doc");
// Path p2=Files.createFile(p1);
// Path p3=Paths.get("k21bp\\firstfile.txt");
// List<String>data=Files.readAllLines(p3);
// Files.write(p2,data);
// System.out.println("File created and data is copied");
// }
// catch(Exception e){
// e.printStackTrace();}}}


// class file {
// public static void main(String args[]) {
// try {
// Path p1=Paths.get("k21bp\\secondfile.doc");
// String data="\n After learning Advance java we got placed in good MNC";
// Files.write(p1,data.getBytes(),StandardOpenOption.APPEND);
// System.out.println("Data Updated in file");
// }
// catch(Exception e)
// {
// System.out.println(e);
// }
// }
// }


class k21bp
{
public static void main(String args[])
{
try
{
Path p1=Paths.get("D:\\k21bp\\secondfile.doc");
List<String> data=Files.readAllLines(p1);
for(String str:data)
{
System.out.println(str);
}
}
catch(Exception e)
{
System.out.println(e);
}
}
}