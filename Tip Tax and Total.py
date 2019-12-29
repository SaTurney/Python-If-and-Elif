# Sabrina Turney
# September 14, 2018
# Program Name: Tip, Tax, and Total
# This program takes the user's input, and calculates tax and tip amount]
# then it adds the tax, tip, and meal price, and displays the total cost.


#Define the main function
def main():
    #I declare all the variables I'm using at float
    #Because we're using money, which isn't always a whole num amount
    taxPercent = 0.06
    tipPercent = 0.0
    mealPrice = 0.0
    totalPrice = 0.0

    #Nice introduction to start the program
    print("Welcome to my meal price calculator.")
    print("This program will accept any priced meal,")
    print("Then it will calculate the cost of the meal with 6% tax and tip!\n")

    #Get the user's meal price to use in the if blocks and calculations
    mealPrice = float(input("Please enter the price of your meal: $ "))
    #taxPercent is updated to reflect how much tax is paid on this meal
    #makes our final calculation clear and concise.
    taxPercent = mealPrice * taxPercent

    #Decision block starts here:
    #The meal price must be between the two values for the block to execute.
    #I update the tip percent depending on the price of the meal
    #This makes calculation at the end clear.
    if mealPrice >= .01 and mealPrice <= 5.99:
        tipPercent = 0.10
        tipPercent = (mealPrice * tipPercent)
    elif mealPrice >= 6.00 and mealPrice <= 12.00:
        tipPercent = 0.13
        tipPercent = (mealPrice * tipPercent)
    elif mealPrice >= 12.01 and mealPrice <= 17.00:
        tipPercent = 0.16
        tipPercent = (mealPrice * tipPercent)
    elif mealPrice >= 17.01 and mealPrice <= 25.00:
        tipPercent = 0.19
        tipPercent = (mealPrice * tipPercent)
    elif mealPrice >= 25.01:
        tipPercent = 0.22
        tipPercent = (mealPrice * tipPercent)

    #All that's left is the caluclation
    #It's very clear now that tax and tip are calculated
    totalPrice = mealPrice + taxPercent + tipPercent
    #The total price is displayed to the user
    #We only need 2 decimal place's worth for our value
    #This makes the statement clear.
    print("The total amount you'll pay for your meal is: $%0.02f" %totalPrice)

#Call the function to start the program for the user.
main()
