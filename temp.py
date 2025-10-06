temperature = float(input("Enter the temperature in °C: "))

if temperature < 20:
    condition = "Cold"
elif 20 <= temperature <= 30:
    condition = "Normal"
else:
    condition = "Hot"

print(f"The weather is {condition}.")