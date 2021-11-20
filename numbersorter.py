# Create a program that ask 4 numbers.
# Print the 4 numbers from highest to lowest using only if-else statement.


# Step 1: Ask four numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

# Step 2: Use if-else statements.
if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 < num4:
    num3, num4 = num4, num3

if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 < num4:
    num3, num4 = num4, num3

if num1 < num2:
    num1, num2 = num2, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 < num4:
    num3, num4 = num4, num3

sequence = num1, num2, num3, num4
# Step 3: Print the 4 numbers from highest to lowest using only if-else statement.
print("The sequence from highest to lowest is:",sequence)