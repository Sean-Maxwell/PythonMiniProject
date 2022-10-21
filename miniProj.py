## The first line will ask the user to input which 
# 
val = 0

endVal = 99

# while Val not equal 99 prompt the 3 options.
while val !=99:
    print("1. Check if a number is odd/even")
    print("2. Square a number")
    print("3. Enter 99 to exit")

    selection = int(input("enter selection : "))

    if selection == 99:
        #Break if the inputted value is 99
        print("Program ended. \n")
        break
    
    elif selection == 1:
        val = int(input("Enter number to check if odd/even : "))
        # Get modulus
        myval = val % 2

        #Check if a number is even or odd
        if myval == 0:
            print("Even\n")
        else:
            print("Odd\n")
   
    elif selection == 2:
        val = int(input("Enter number to be squared : "))
        print(val ** 2 ,"\n")
    
    else:
        print("Invalid selection\n")