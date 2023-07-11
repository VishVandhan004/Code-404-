import java.io.*;
class FDS {
    public static void main(String args[]) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       System.out.println("Enter a file name: ");
       FileOutputStream fos = new FileOutputStream("abc.txt");
       fos.write(101);
       fos.close();
       String fname = br.readLine();
       File f = new File(fname);
       String result = f.exists() ? "exists" : "does not exist";
       System.out.println("the given file: "+result);
       if(f.exists()){
        result = f.canRead() ? "readable" : "not readable";
        System.out.println("the given file is"+result+f.getAbsolutePath());
        result = f.canWrite() ? "writable" : "not writable";
        System.out.println("the given file is:  "+result);
        System.out.println("the given file length is "+f.length() + "in bytes");
        if(fname.endsWith(".jpg") || fname.endsWith(".png")|| fname.endsWith(".gif")){
            System.out.println("this is an image file");
        }
        else if(fname.endsWith(".exe")){
            System.out.println("this is an executable file");
        }
        else if(fname.endsWith(".txt")){
            System.out.println("this is a text file");
        }
        else {
            System.out.println("Unknown file");
        }
       } 
    }
}