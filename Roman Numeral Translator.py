# Sabrina Turney
# Program Name: Roman Numerals
# Program Description: this program will ask user for a number 1-10 
# and will display the roman numeral corresponding to that number
# if the number is less than one or greater than ten
# an error message will display.


# Define the main function
def main():
    #These are the Roman numeral equivalents. 
    #I = 1
    #II = 2
    #III = 3
    #IV = 4
    #V = 5
    #VI = 6
    #VII = 7
    #VIII = 8
    #IX = 9
    #X = 10
    
    # Define variables
    userNumber = 0     # integer numbers for Roman numerals.
    romanNumber = 0

    #Descriptive user introduction!
    print("Welcome to my Roman numeral converter.")
    print("This program will accept any whole number 1 through 10,")
    print("Then it will convert it into a Roman numeral!\n")

    
    # I use int here because the program needs a whole number value
    userNumber = eval(input("Please enter a number between 1 and 10: "))

# ****** The Decision Structure ********
    #The If/else structure will test the criteria and execute the first print
    #statement if the condition is true, if it is not true it will skip that one
    #and then check the elif criteria. If it is true it will execute that print
    #statement. If it is not true it will skip it and move on.
    if userNumber >10: # if the number is too large
        print("Your number is greater than ten!")
    elif userNumber < 1: # if the number is too small
        print("Your number is less than one!")
    elif userNumber != int:
        print("Please print a whole number value.")
    else:
        # if no errors are detected
        # we print the Roman numeral value
        if userNumber == 1:
            romanNumber = "I"
        elif userNumber == 2:
            romanNumber = "II"
        elif userNumber == 3:
            romanNumber = "III"
        elif userNumber == 4:
            romanNumber = "IV"
        elif userNumber == 5:
            romanNumber = "V"
        elif userNumber == 6:
            romanNumber = "VI"
        elif userNumber == 7:
            romanNumber = "VII"
        elif userNumber == 8:
            romanNumber = "VIII"
        elif userNumber == 9:
            romanNumber = "IX"
        elif userNumber == 10:
            romanNumber = "X"
        #Now that we know what the Roman numeral value is,
        #we print it to the user.
        print (f"The Roman numeral for your number, {userNumber}, is {romanNumber}.")
    

#call the funciton for the user
main()
                        
                
                    
  
    
    
