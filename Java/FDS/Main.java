import java.util.*;
class Main {
    public static void main(String args[]) {
        // HASHSET COLLECTION FRAMEWORK
        HashSet<String> s = new HashSet<>();
        // adding elements
        s.add("Aashish");
        s.add("Guna");
        s.add("Mia");
        s.add("Mia"); // redundant or duplicate data
        // checking set size
        int size = s.size();
        System.out.println(size);
        // check if element exists
        boolean contains = s.contains("Mia");
        System.out.println(contains);
        // iterating over elements
        for(String e: s){
            System.out.println(e);
        }
        // remove element
        s.remove("Mia");
        // clear the whole set
        s.clear();
        }
    }