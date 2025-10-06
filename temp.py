
celsius = float(input("Enter the temperature in °C: "))

fahrenheit = (celsius * 9/5) + 32

if celsius < 20:
    condition = "Cold"
elif 20 <= celsius <= 30:
    condition = "Normal"
else:
    condition = "Hot"

print("\n--- Temperature Report ---")
print(f"Temperature in Celsius: {celsius:.2f}°C")
print(f"Condition: {condition}")
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")