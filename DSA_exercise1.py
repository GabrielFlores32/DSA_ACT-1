#Create a program that converts temperatures between Celsius and Fahrenheit.

#Ask the user to input a temperature.
temperature = float(input("Enter the value of the temperature: "))

#Ask the user to select the conversion type
print("select the type of conversion:")
print("Type 1 for Celsius to Fahrenheit and type 2 for Fahrenheit to Celsius")
conversion = int(input("Enter your choice: "))

#Perform the appropriate conversion and print the result.
if conversion == 1:
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C.")
    
elif conversion == 2:
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit}°F.")
    
else:
    print("Invalid choice. Please select 1 or 2.") 