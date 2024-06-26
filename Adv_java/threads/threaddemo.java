package threads;

class threaddemo extends Thread 
{ 
public void run() 
{ 
System.out.println("Priority of thread:- "+ Thread.currentThread().getPriority()); 
} 
@SuppressWarnings("deprecation")
public static void main(String args[]) 
{ 
threaddemo t=new threaddemo(); 
t.start(); 
System.out.println(t.getName()); 
t.setPriority(Thread.MIN_PRIORITY); 
System.out.println(t.getId()); 
System.out.println(t.isAlive()); 
} 
}
