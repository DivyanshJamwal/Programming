package Coding_Practice.JAVA;

import java.io.File;
import java.io.IOException;
class Main {
public static void main(String[] args) {
File f = new File("file1.txt");

try {
if(f.createNewFile()) {
System.out.println("File created successfully!");
}
else System.out.println("File already exist");
}
catch (IOException ioe) {
System.out.println("Some error occured while creating file");
}

System.out.println("isFile(): "+f.isFile());
System.out.println("isDirectory(): "+f.isDirectory());
System.out.println("isHidden(): "+f.isHidden());
System.out.println("exists(): "+f.exists() );
System.out.println("canRead(): "+f.canRead());
System.out.println("canWrite(): "+f.canWrite());
System.out.println("getName(): "+f.getName());
System.out.println("getPath(): "+f.getPath());
System.out.println("getAbsolutePath(): "+f.getAbsolutePath());
System.out.println("lastModified(): "+f.lastModified());
System.out.println("length(): "+f.length());
File f2 = new File("file2.txt");
System.out.println(f.renameTo(f2));
if(f.delete()) System.out.println("deleted"); else System.out.println("not deleted");

File p = new File("/Users/jeevanbala/IdeaProjects/First/src");
File[] files = p.listFiles();
for(File filex:files) {
System.out.println(filex.getName());
}


}
}