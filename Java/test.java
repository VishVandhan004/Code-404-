import java.awt.*;
import java.awt.event.*;

public class test {
   private Frame frame;
   private TextField displayField;

   public test() {
      frame = new Frame("Calculator");
      displayField = new TextField(20);
   }

   public void createUI() {
      Panel buttonpanel = new Panel();
      buttonpanel.setLayout(new GridLayout(4, 4));
      Button b1 = new Button("1");
      Button b2 = new Button("2");
      // Button b3 = new Button("3");
      // Button b4 = new Button("4");
      // Button b5 = new Button("5");
      // Button b6 = new Button("6");
      // Button b7 = new Button("7");
      // Button b8 = new Button("8");
      // Button b9 = new Button("9");
      // Button b0 = new Button("0");
      Button buttonplus = new Button("+");
      // Button buttonminus = new Button("-");
      // Button buttonproduct = new Button("*");
      // Button buttondivide = new Button("/");
      // Button buttonequals = new Button("=");
      buttonpanel.add(b1);
      buttonpanel.add(b2);
      // buttonpanel.add(b3);
      // buttonpanel.add(b4);
      // buttonpanel.add(b5);
      // buttonpanel.add(b6);
      // buttonpanel.add(b7);
      // buttonpanel.add(b8);
      // buttonpanel.add(b9);
      // buttonpanel.add(b0);
      buttonpanel.add(buttonplus);
      // buttonpanel.add(buttonminus);
      // buttonpanel.add(buttonproduct);
      // buttonpanel.add(buttondivide);
      // buttonpanel.add(buttonequals);
      b1.addActionListener(new ButtonClickListener());
      b2.addActionListener(new ButtonClickListener());
      // b3.addActionListener(new ButtonClickListener());
      // b4.addActionListener(new ButtonClickListener());
      // b5.addActionListener(new ButtonClickListener());
      // b6.addActionListener(new ButtonClickListener());
      // b7.addActionListener(new ButtonClickListener());
      // b8.addActionListener(new ButtonClickListener());
      // b9.addActionListener(new ButtonClickListener());
      // b0.addActionListener(new ButtonClickListener());
      buttonplus.addActionListener(new ButtonClickListener());
      // buttonminus.addActionListener(new ButtonClickListener());
      // buttonproduct.addActionListener(new ButtonClickListener());
      // buttondivide.addActionListener(new ButtonClickListener());
      // buttonequals.addActionListener(new ButtonClickListener());

      displayField.setEditable(false);

      frame.add(displayField, BorderLayout.NORTH);
      frame.add(displayField, BorderLayout.CENTER);

      frame.setSize(300, 300);
      frame.setVisible(true);
   }
   private class ButtonClickListener implements ActionListener {
      public void action(ActionEvent event) {
         String buttontext = ((Button) event.getSource()).getLabel();
         String display = displayField.getText();
         if (buttontext.equals("=")) {
            try {
               double result = evaluateExpression(display);
               displayField.setText(String.valueOf(result));
            } catch (NumberFormatException e) {
               displayField.setText("Error");
            }
         } else {
            displayField.setText(display + buttontext);
         }
      }

      public double evaluateExpression(String expression) {
         String[] tokens = expression.split("\\+");
         double operand1 = Double.parseDouble(tokens[0]);
         double operand2 = Double.parseDouble(tokens[1]);
         // double operand3 = Double.parseDouble(tokens[2]);
         // double operand4 = Double.parseDouble(tokens[3]);
         // double operand5 = Double.parseDouble(tokens[4]);
         // double operand6 = Double.parseDouble(tokens[5]);
         // double operand7 = Double.parseDouble(tokens[6]);
         // double operand8 = Double.parseDouble(tokens[7]);
         // double operand9 = Double.parseDouble(tokens[8]);
         // double operand0 = Double.parseDouble(tokens[9]);
         return operand1 + operand2;
      }
   }

   public static void main(String args[]) {
      test calculator = new test();
      calculator.createUI();
   }

}