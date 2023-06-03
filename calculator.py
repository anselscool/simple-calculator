# This function adds two numbers
def add(x, y):
  return x + y

# This function subtracts two numbers
def subtract(x, y):
  return x - y

# This function multiplies two numbers
def multiply(x, y):
  return x * y

# This function devides two numbers
def divide(x, y):
  return x / y

# Displays mathamatical operations
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
  # Promts you to chose an operation
  choice = input("Enter choice(1/2/3/4): ")

  # Checks if choice is one of the four options
  if choice in ('1', '2', '3', '4'):
    try:
      # Asks you to enter the first number
      num1 = float(input("Enter first number: "))
      # Asks you to enter the second number
      num2 = float(input("Enter second number: "))
    except ValueError:
      # If you entered invalid option it will ask again for a number
      print("Invalid input. Please enter a number.")
      continue

    # If you chose 1 then it will add two numbers
    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    # If you chose 2 then it will subtract two numbers
    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    # If you chose 3 then it will multiply two numbers
    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

    # If you chose 4 then it will divide two numbers
    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

    # Asks if the user would like another calculation
    # Break the while loop if answer is no
    next_calculation = input(
      "Would you like to do another calculation? (yes/no): ")
    if next_calculation == "no":
      break
  else:
    print("Invalid Input")
