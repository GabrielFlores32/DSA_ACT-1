print ("Type the corresponding numbers: ")
print ("1 = Voltage calculator")
print ("2 = Resistance calculator")
print ("3 = Current calculator")

choice = int(input("Betlog?: "))

if choice == 1 :
    resistance = int(input("Resistance: "))
    current = int(input("Current: "))
    answer = resistance*current
    print(f"The Voltage is {answer}")

elif choice == 2 :
    voltage = int(input("Voltage: "))
    current = int(input("Current: "))
    answer = voltage/current
    print(f"The Resistance is {answer}")
    
elif choice == 3 :
    voltage = int(input("Voltage: "))
    resistance = int(input("Resistance: "))
    answer = voltage/resistance
    print(f"The Resistance is {answer}")
    
else:
    print("Please enter a valid number")