print ("Type the corresponding numbers: ")
print ("1 = Voltage calculator")
print ("2 = Resistance calculator")
print ("3 = Current calculator")

choice = int(input("Betlog?: "))

if choice == 1 :
    resistance = float(input("Resistance: "))
    current = float(input("Current: "))
    answer = resistance*current
    print(f"The Voltage is {answer}")

elif choice == 2 :
    voltage = float(input("Voltage: "))
    current = float(input("Current: "))
    answer = voltage/current
    print(f"The Resistance is {answer}")
    
elif choice == 3 :
    voltage = float(input("Voltage: "))
    resistance = float(input("Resistance: "))
    answer = voltage/resistance
    print(f"The Resistance is {answer}")
    
else:
    print("Please enter a valid number")