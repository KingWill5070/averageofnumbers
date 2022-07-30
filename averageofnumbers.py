#Harold Williams
#June 2, 2022
#This program finds an average of numbers entered by user

def main():
    countofNumbers = 0
    number = average= total = 0.0

    countofNumbers = int(input("How many numbers are there?: ")) #5

    #Use a counted loop to ask the user to enter the numbers
    for i in range(countofNumbers): #Will repeat 5 times
        number = float(input("Please enter a number: ")) #
        #This will allow us to keep the number entered and add it to total
        total += number # 2 first time, then 2+4 = 6 2nd etc....


    average = total / countofNumbers
    print(f"The average of your numbers is {average}")



main()
