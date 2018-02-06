import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.*;

import jdk.nashorn.internal.parser.Scanner;
public class fileWalker{

    private ArrayList<String>fileNameArray=new ArrayList<String>();

    public void fileLister(String path) {
     
        File srcDir= new File(path);
        // if(srcDir.isDirectory())
            // System.out.println("Path is a directory");
        // else if(srcDir.isFile())
            // System.out.println("Path is file");
        if(srcDir.isDirectory()){
            File[] fileList = srcDir.listFiles();
            for(File file:fileList){
                if(file.isDirectory()){
                    fileLister(file.getAbsolutePath());
                }
                else{
                    this.fileNameArray.add(file.getAbsolutePath());
                    // System.out.println(file.getAbsolutePath());
                    
                }
            }
        }
    }

    public void serachFileType(String fileType,String path){
        File srcDFile= new File(path);
        if(srcDFile.isDirectory()){
            try{
            fileLister(path);//This will initialize the array list with file names
            }
            catch(Exception e){
                e.printStackTrace();
            }
        }
        if(this.fileNameArray.size()>0){
            for(String fName:fileNameArray){
                // String[]temp=fName.split(File.separatorChar);
                // String name=temp[temp.length-1];
                File lFile=new File(fName);
                if(lFile.getName().contains(fileType)){
                    System.out.println(fName);
                }
            }
        }
        
    }

    public void deleteFiles(String fileType,String path) {
        File srcDFile= new File(path);
        if(srcDFile.isDirectory()){
            try{
            fileLister(path);//This will initialize the array list with file names
            }
            catch(Exception e){
                e.printStackTrace();
            }
        }
        if(this.fileNameArray.size()>0){
            for(String fName:fileNameArray){
                // String[]temp=fName.split(File.separatorChar);
                // String name=temp[temp.length-1];
                File lFile=new File(fName);
                if(lFile.getName().contains(fileType)){
                    System.out.println(fName);
                    lFile.delete();//Deleting a file at a time.
                }
            }
        }
        
    }

    public static void main(String[] args) {
        fileWalker obFileWalker=new fileWalker();
        try{
            // obFileWalker.fileLister("..");
            //Scanner sc=new Scanner(System.in);
            BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
            String fileType= bfr.readLine();
            String directory = bfr.readLine();
            obFileWalker.deleteFiles(fileType,directory);
        }
        catch(NullPointerException e){
            System.err.println(e.getStackTrace());
        }
        catch(Exception e){
            e.printStackTrace();
            System.err.println(e.getMessage());
        }
    }
}