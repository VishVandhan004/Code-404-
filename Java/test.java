package Java;
import java.awt.*;
import java.awt.event.*;

class test {
    private Frame frame;
    private TextField displayField;

    public test() {
        frame = new Frame("Calculator");
        displayField = new TextField(20);
    }

    public void createUI() {
        Panel buttonPanel = new Panel();
        buttonPanel.setLayout(new GridLayout(5, 4));

        // Creating buttons for numbers 0 to 9
        for (int i = 0; i <= 9; i++) {
            Button numberButton = new Button(Integer.toString(i));
            numberButton.addActionListener(new ButtonClickListener());
            buttonPanel.add(numberButton);
        }

        // Creating operator buttons
        Button buttonPlus = new Button("+");
        Button buttonMinus = new Button("-");
        Button buttonMultiply = new Button("*");
        Button buttonDivide = new Button("/");
        Button buttonEquals = new Button("=");
        Button buttonDelete = new Button("Delete");

        // Adding operator buttons and delete button to the panel
        buttonPanel.add(buttonPlus);
        buttonPanel.add(buttonMinus);
        buttonPanel.add(buttonMultiply);
        buttonPanel.add(buttonDivide);
        buttonPanel.add(buttonEquals);
        buttonPanel.add(buttonDelete);

        // Setting up button click listeners for operator buttons and delete button
        buttonPlus.addActionListener(new ButtonClickListener());
        buttonMinus.addActionListener(new ButtonClickListener());
        buttonMultiply.addActionListener(new ButtonClickListener());
        buttonDivide.addActionListener(new ButtonClickListener());
        buttonEquals.addActionListener(new ButtonClickListener());
        buttonDelete.addActionListener(new ButtonClickListener());

        // Setting up the display field
        displayField.setEditable(false);

        // Adding components to the frame
        frame.add(displayField, BorderLayout.NORTH);
        frame.add(buttonPanel, BorderLayout.CENTER);

        // Setting up frame properties
        frame.setSize(300, 300);
        frame.setVisible(true);
    }

    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String buttonText = ((Button) event.getSource()).getLabel();
            String displayText = displayField.getText();

            if (buttonText.equals("=")) {
                try {
                    double result = evaluateExpression(displayText);
                    displayField.setText(String.valueOf(result));
                } catch (NumberFormatException e) {
                    displayField.setText("ERROR");
                }
            } else if (buttonText.equals("Delete")) {
                if (!displayText.isEmpty()) {
                    displayText = displayText.substring(0, displayText.length() - 1);
                    displayField.setText(displayText);
                }
            } else {
                displayField.setText(displayText + buttonText);
            }
        }

        private double evaluateExpression(String expression) {
            String[] tokens;
            double operand1;
            double operand2;

            if (expression.contains("+")) {
                tokens = expression.split("\\+");
                operand1 = Double.parseDouble(tokens[0]);
                operand2 = Double.parseDouble(tokens[1]);
                return operand1 + operand2;
            } else if (expression.contains("-")) {
                tokens = expression.split("-");
                operand1 = Double.parseDouble(tokens[0]);
                operand2 = Double.parseDouble(tokens[1]);
                return operand1 - operand2;
            } else if (expression.contains("*")) {
                tokens = expression.split("\\*");
                operand1 = Double.parseDouble(tokens[0]);
                operand2 = Double.parseDouble(tokens[1]);
                return operand1 * operand2;
            } else if (expression.contains("/")) {
                tokens = expression.split("/");
                operand1 = Double.parseDouble(tokens[0]);
                operand2 = Double.parseDouble(tokens[1]);
                if (operand2 != 0) {
                    return operand1 / operand2;
                } else {
                    throw new ArithmeticException("Division by zero");
                }
            }

            return 0; // Default return value if the expression is not supported
        }
    }

    public static void main(String[] args) {
        test calculator = new test();
        calculator.createUI();
    }
}