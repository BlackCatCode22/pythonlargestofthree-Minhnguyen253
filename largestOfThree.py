# largestOfThree.py
# dH 2/25/23

print("Minh Nguyen 0920131\n")
print("CIT-95 Python SP23")
print("\nThis is the Largest of Three program...")
# input three integers from the user.
n1 = input("\nPlease enter your first integer: ")
n2 = input("\nPlease enter your second integer: ")
n3 = input("\nPlease enter your third and last integer: ")

print("first integer = " + n1 + " , second integer = " + n2 + " and last integer = " + n3)

# Find the largest
# Check if n1 is the largest number:
if n1 >= n2 and n1 >= n3:
    largest = n1
# Check if n2 is the largest number:
elif n2 >= n1 and n2 >= n3:
    largest = n2
# Check if n3 is the largest number:
else:
    largest = n3

# output the largest
print("The largest number is ", largest)

# find the sum
the_sum = int(n1) + int(n2) + int(n3)

# output the sum
print("The sum of " + n1 + " and " + n2 + " and " + n3 + " is " + str(the_sum))
