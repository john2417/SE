/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package gradle_test_1;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
        App csvRedaer = new App();
        csvRedaer.readCSV();
        System.out.println(new App().readCSV());
    }

    public List<List<String>> readCSV() {
        List<List<String>> csvList = new ArrayList<List<String>>();
        File csv = new File("H:/SE/SE/books.csv");
        BufferedReader br = null;
        String line ="";

        try{
            br = new BufferedReader(new FileReader(csv));
            while ((line = br.readLine())!= null) {
                List<String> aLine = new ArrayList<String>();
                String[] lineArr = line.split(",");
                aLine = Arrays.asList(lineArr);
                csvList.add(aLine);
            }

        }catch (FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        } finally{
            try{
                if(br!=null){
                    br.close();
                }
            }catch(IOException e){
                e.printStackTrace();
            }

        }return csvList;
    }


}