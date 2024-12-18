import streamlit as st

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Streamlit App
def calculator():
    st.title("Simple Calculator")
    st.write("This is a simple calculator built with Streamlit.")

    # User input for numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    # Dropdown for operation selection
    operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform the selected operation
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.write(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    calculator()
