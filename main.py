
print("Select The Operation To Perform")
print("                                       ")
print("1. Area Of Rectangle")
print("2. Perimeter Of Rectangle")
print("                                       ")
print("3. Area Of square ")
print("4. Perimeter Of Square")
print("                                       ")
print("5. Area Of Circle")
print("6. Perimeter Of Circle")
print("                                       ")
print("7. Area Of Triangle")
print("8. Perimeter Of Triangle")
print("                                       ")

while True:
    # take input from the user
    choice = input("Enter Choise ( 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 ): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):


        if choice == '1':
            num1 = float(input("Enter Length: "))
            num2 = float(input("Enter Breadth: "))
            print('Area Of Rectangle = ', (num1 * num2))

        elif choice == '2':
            num1 = float(input("Enter Length: "))
            num2 = float(input("Enter Breadth: "))
            print( "Perimeter Of Rectangle = ", (2*(num1+num2)))

        elif choice == '3':
            num1 = float(input("Enter Side: "))
            print('Area Of Square = ', (num1 ** 2))

        elif choice == '4':
            num1 = float(input("Enter Side: "))
            print('Perimeter Of Square = ', (4 * num1))
        
        elif choice == '5':
            num1 = float(input("Enter Radius Of Circle: "))
            pi = 3.14
            print('Area Of Circle = ', (pi * (num1 ** 2)))
            
        elif choice == '6':
            num1 = float(input("Enter Radius Of Circle: "))
            pi = 3.14
            print('Perimeter Of Circle = ', (pi * (num1 * 2)))
            
        elif choice == '7':
            num1 = float(input("Enter Side A Of Triangle: "))
            num2 = float(input("Enter Side B Of Triangle: "))
            num3 = float(input("Enter Side C Of Triangle: "))
            
            s = (num1 + num2 + num3)/2
            ar = (s*(s-num1)*(s-num2)*(s-num3))**0.5
            
            print('Area Of Triangle = ', ar)
            
        elif choice == '8':
            num1 = float(input("Enter Side A Of Triangle: "))
            num2 = float(input("Enter Side B Of Triangle: "))
            num3 = float(input("Enter Side C Of Triangle: "))

            print('Perimeter Of Circle = ', (num1+num2+num3))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Would You Like To Perform A New Calculation ? ( Yes / No ) : ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
