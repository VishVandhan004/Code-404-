import java.awt.*;
public class test extends Frame
{
     test(){
        Label firstname = new Label ("First Name");
        firstname.setBounds(20, 50, 80, 20);
        add(firstname);
        TextField tf = new TextField();
        tf.setBounds(50, 70, 80, 20);
        add(tf);
        setTitle("myawt");
        setSize(600,600);
        setLayout(null);
        setVisible(true);
        Label lastname = new Label ("Last Name");
        lastname.setBounds(20, 50, 80, 20);
        add(lastname);
        TextField tf1 = new TextField();
        tf1.setBounds(50, 70, 80, 20);
        add(tf1);
        setLayout(null);
        setVisible(true);
     }
     public static void main(String args[]){
        test awt = new test();
     }
}